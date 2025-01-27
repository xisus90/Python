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


    def data_db(self, list_titles, list_prices):

        list_titles = [title.strip() for title in list_titles]
        min_length = min(len(list_titles), len(list_prices))

  
        for p in range(min_length):

            current_title = list_titles[p]
            current_price = float(list_prices[p])

            self._cursor.execute(""" SELECT Gamesnames, Gamesprices, date
                                    FROM games
                                    WHERE Gamesnames = %s""", (current_title,))
            result = self._cursor.fetchone()

            if result:
                db_price = float(result[1])
                if current_price < db_price:
                    print (f"el juego {current_title} tiene un precio menor\n el precio actual es {list_prices[p]}€ y el precio anterior es {db_price}€")
                if db_price == current_price:
                    print (f"el precio del juego {current_title} es igual")

        #actual_date = date.today()
        #data_to_insert = [(title, price, actual_date) for title, price in zip(gametitle, gameprice)]
        
        #self._cursor.executemany("""
        #    INSERT IGNORE INTO games ( Gamesnames, Gamesprices, Date)
        #    VALUES (%s, %s, %s)
        #    """, data_to_insert)

        #self._connection.commit()
        #print("datos insertados correctamente")

        self._cursor.close()
        self._connection.close()

class ScarpGames:

    def __init__(self):
        
            self._data_titles = []
            self._data_prices = []

    def search(self):
   
        self.Lookingdataprice()
        Database().data_db(self._data_titles, self._data_prices)
        
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