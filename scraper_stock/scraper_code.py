import re
import pymysql
import requests
from bs4 import BeautifulSoup
from datetime import date

class Database:
    
    def __init__(self):
        
        self._connection = pymysql.connect(
        host="localhost", 
        user="root",
        password="root",
        db="gamelist"
        )
        
        self._cursor = self._connection.cursor()


    def data_db(self, gametitle, gameprice):

        #actual_date = date.today()
        #data_to_insert = [(title, price, actual_date) for title, price in zip(gametitle, gameprice)]
        
        #self._cursor.executemany("""
        #    INSERT IGNORE INTO games ( Gamesnames, Gamesprices, Date)
        #    VALUES (%s, %s, %s)
        #    """, data_to_insert)

        #self._connection.commit()
        #print("datos insertados correctamente")

        self._cursor.execute(" SELECT Gamesnames, Gamesprices, date FROM games ")
        results = self._cursor.fetchall()


        gameprice = [float(price) for price in gameprice]

        min_length = min(len(results), len(gameprice))

        for i in range(min_length):

            db_price = float(results[i][1])

            if db_price < gameprice[i]:
                print (f"el juego {gametitle[i]} tiene un precio menor\n el precio actual es {gameprice[i]}€ y el precio anterior es {db_price}€")
            if db_price == gameprice[i]:
                print (f"el precio del juego {gametitle[i]} es igual")

            

     



        self._cursor.close()
        self._connection.close()

class ScarpGames:

    def __init__(self):
        
            self._data_titles = []
            self._data_prices = []

    def search(self):
   
        price_game = self.Lookingdataprice()
        insertdb = Database().data_db(self._data_titles, self._data_prices)
        
    def Lookingdataprice(self):
 
        data_url = "https://www.dlcompare.es/juegos"
        result = requests.get(data_url)
        print(result)

        if result.status_code == 200:
            filter = BeautifulSoup(result.text, "html.parser")
            
            game_titles = filter.find_all('span', {'class':'name'})
            game_prices = filter.find_all('span', {'class': 'price'})

            for game_title in game_titles:
                game_text = game_title.text.split()
                cleaned_game_text = ' '.join(game_text)
                self._data_titles.append(cleaned_game_text)
            
            for game_price in game_prices:
                price_text = game_price.text.split()
                cleaned_price_text = ' '.join(price_text)
                self._data_prices.append(cleaned_price_text)   



ScarpGames().search()