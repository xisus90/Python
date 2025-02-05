from send_mails import AutoMails
from data_code import Database_UserGames
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List
import pymysql
from datetime import date


@dataclass
class Game:
    title: str
    price: float  


class Database_Scraper:
    

    def __init__(self):
        
        """Inicializa la conexión a la base de datos"""
        try:
            self._connection = pymysql.connect(
                host="localhost", 
                user="root",
                password="root",
                db="gamelist"
            )
            self._cursor = self._connection.cursor()
        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")
            self._connection = None
            self._cursor = None
            

    def close_connection(self):

        """Cierra la conexión y el cursor correctamente"""
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()
        print("🔒 Conexión cerrada correctamente.")


    def comparate_prices(self, games : List [Game]):


        for game in games:
            current_title = game.title
            current_price = float(game.price)

            self._cursor.execute(""" SELECT Gamesnames, Gamesprices, date
                                    FROM games
                                    WHERE Gamesnames = %s""", (current_title,))
            result = self._cursor.fetchone()

            if result:
                db_price = float(result[1])
                if current_price < db_price:
                        mails_for_game = Database_UserGames().get_mail_for_game(current_title)
                        if mails_for_game:
                                AutoMails.Sendmail(mails_for_game, current_title, current_price, db_price)

        self._connection.close()


    def actu_db_games(self, games: List[Game]):


        actual_date = date.today()
        data_to_insert = [(game.title, game.price, actual_date) for game in games]  
        
        self._cursor.executemany("""
            INSERT IGNORE INTO games ( Gamesnames, Gamesprices, Date)
            VALUES (%s, %s, %s)
            """, data_to_insert)

        self._connection.commit()
        print("datos insertados correctamente")


class Scraper:

    def __init__(self):
        self._data_titles = []
        self._data_prices = []
        self._data_db = Database_Scraper()


    def Lookingdataprice(self) -> List[Game]:
        """Extrae los títulos y precios de los juegos de la web."""
        
        data_url = "https://www.dlcompare.es/juegos"
        result = requests.get(data_url)
        
        if result.status_code != 200:
            print(" Error al obtener los datos de la página.")
            return []

        #  Parsear HTML correctamente
        filter = BeautifulSoup(result.text, "html.parser")

        game_titles = filter.find_all('span', {'class': 'name'})
        game_prices = filter.find_all('span', {'class': 'price'})

        games = []

        for title, price in zip(game_titles, game_prices):
            game_text = ' '.join(title.text.split())  # Limpiar texto
            price_text = price.text.replace("€", "").replace(",", ".").strip()  # Limpiar precio

            try:
                price_value = float(price_text)  # Convertir a float
            except ValueError:
                price_value = 0.0  # Si no se puede convertir, asigna 0.0

            games.append(Game(game_text, price_value))  #  Agregar el objeto Game

        return games  # Retorna la lista de juegos

    def execute(self):

        games_list = self.Lookingdataprice()
        self._data_db.actu_db_games(games_list)
        self._data_db.comparate_prices(games_list)


Scraper().execute()