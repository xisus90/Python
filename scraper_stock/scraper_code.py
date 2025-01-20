import re
import pymysql
import requests
from bs4 import BeautifulSoup

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

 

        data_to_insert = list(zip(gametitle, gameprice))

        self._cursor.executemany("""
            INSERT INTO games ( Gamesnames, Gamesprices)
            VALUES (%s, %s)
            """, (data_to_insert))

        # Confirmar los cambios en la base de datos
        self._connection.commit()
        print("datos insertados correctamente")
        
        self._cursor.close()
        self._connection.close()
        print("conexion cerrada")



class SearchGame:

    #def __init__(self, game):       
    #        self._game = game


    def search(self):
   
        price_game = self.Lookingdataprice()
        insertdb = Database().data_db(self._data_titles, self._data_prices)
        return insertdb


    def Lookingdataprice(self):
 
        data_url = "https://www.dlcompare.es/juegos"
        result = requests.get(data_url)
        print(result)

        if result.status_code == 200:
            filter = BeautifulSoup(result.text, "html.parser")
            
            game_titles = filter.find_all('span', {'class':'name'})
            game_prices = filter.find_all('span', {'class': 'price'})

            self._data_titles = []
            self._data_prices = []

            for game_title in game_titles:
                game_text = game_title.text.split()
                cleaned_game_text = ' '.join(game_text)
                self._data_titles.append(cleaned_game_text)
            
            for game_price in game_prices:
                price_text = game_price.text.split()
                cleaned_price_text = ' '.join(price_text)
                self._data_prices.append(cleaned_price_text)   

            lenght = 0 
            while lenght <= len(self._data_titles)-1:
                print(f"{self._data_titles[lenght]} --> {self._data_prices[lenght]}€")
                lenght+=1


