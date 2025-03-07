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
                db="usergames"
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


    def get_datas_from_DB(self) -> dict:

        """Obtiene todos los juegos con sus precios más recientes de la base de datos."""
        
        self._cursor.execute("""
            SELECT Gamesnames, Gamesprices, date
            FROM games
            WHERE date = (SELECT MAX(date) FROM games WHERE games.Gamesnames = Gamesnames)
        """)
        
        results = self._cursor.fetchall()  

        # Convertir resultados a un diccionario para acceso rápido
        price_dict = {title: float(price) for title, price, _ in results}
        
        return price_dict
        

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


    def compare_price(self, games: List[Game], db_prices: dict):
        """Compara los precios del scraper con los de la base de datos."""
        
        for game in games:
            current_title = game.title
            current_price = float(game.price)

            if current_title in db_prices:
                previous_price = db_prices[current_title]  # ✅ Precio anterior específico

                if current_price < previous_price:
                    mails_for_game = Database_UserGames().get_mail_for_game(current_title)
                    if mails_for_game:
                        print(f""" {mails_for_game} --> juego: {current_title}
                        """)
                    AutoMails.Sendmail(mails_for_game, current_title, current_price, previous_price)


    def execute(self):

        games_list = self.Lookingdataprice()
        if games_list:
            pricestocompare = self._data_db.get_datas_from_DB()
            #self.compare_price(games_list, pricestocompare)
            self._data_db.actu_db_games(games_list)
            


Scraper().execute()