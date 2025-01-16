import re
import pymysql
import requests
from bs4 import BeautifulSoup

class Database:
    
    def __init__(self):
        
        self.connection = pymysql.connector.connect(
        host="localhost", 
        user="root",
        password="root",
        db="gamelist"
        )

        self.cursor = self.connection.cursor()


class SearchGame:

    def __init__(self, game):       
            self._game = game


    def search(self):
   
        price_game = self.Lookingdataprice()
        return price_game


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

            length = 0 
            while length <= len(self._data_titles)-1:
                print(f"{self._data_titles[length]} --> {self._data_prices[length]}€")
                length+=1

    def data_db(self):

        pass