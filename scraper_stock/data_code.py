import pymysql
import csv
from typing import Optional

class Database:
    
    def __init__(self):
        self._connection = pymysql.connect(
        host="localhost", 
        user="root",
        password="root",
        db="gamelist"
        )
         
        self._cursor = self._connection.cursor()

    def close(self):
        self._cursor.close()
        self._connection.close()
        print("conexion cerrada")


    def findprice(self, game: str) -> Optional[float]:
        
        self._cursor.execute("SELECT Gamesprices FROM games WHERE Gamesnames = %s", (game))
        result = self._cursor.fetchone()

        if not result:
            return None
        return result[0] 
    

    def mail_exists(self, mail) -> bool:
        mail = mail.strip().lower()
        self._cursor.execute("SELECT EmailUser FROM users WHERE EmailUser = %s", (mail,))
        result = self._cursor.fetchone()

        return bool(result)
    

    def new_user(self, mail, game):
    
        if not self.mail_exists(mail):
            print("El email ya existe.")
            return None

        self._cursor.execute("""INSERT INTO users (EmailUser, GameName)
                                VALUES (%s, %s)""", (mail, game))
        
        print("usuario suscrito correctamente")
        self._connection.commit()
        


    def get_game_for_user(self, mail):
        mail = mail.strip().lower()
        self._cursor.execute("SELECT GameName FROM users WHERE EmailUser = %s", (mail,))
        results = self._cursor.fetchall()

        if not results:
            self.close()
            return None
        game_list = [result[0] for result in results]

        self.close()
        return game_list 

    
    def user_to_game(self, game):
        game = game.strip().lower()
        self._cursor.execute("SELECT EmailUser FROM users WHERE GameName = %s", (game,))
        results = self._cursor.fetchall()


        if not results:
            return None
        return results[0]


    def update_db_user(self, mail, game):

        update = """
        UPDATE users
        SET GameName = CONCAT(GameName, ', ', %s)
        WHERE EmailUser = %s
             """
        
        self._cursor.execute(update, (game, mail))
        self._connection.commit() 
        print(f"Juego añadido correctamente al usuario {mail}.")


class SuscriptionsMenu:
    def __init__(self):
        self._data = Database()
        

    def suscription(self, mail, game):
        self._data.new_user(mail, game)
        self._data.close()
    
    def suscriptorgames(self, mail):
        if not self._data.mail_exists(mail):
               return None
        #self._data.close()
        return self._data.get_game_for_user(mail)
    

class ActionGetPrice:

    def __init__(self):
       self._data = Database()


    def Execute(self, game):
        gameprice = self._data.findprice(game)

        self._data.close()
        return gameprice
    



#class ActionAlertWhenPriceIsCheaper:
#    def __init__(self, data, mail_client):
#        self._data = data
#        self._mail_client = mail_client

#    def Execute(self, game, price):
#        suscritors = self._data.getAllSuscritors(game)
#        self._data.close()

#        for suscriptor in suscritors:
#            self._mail_client.send_mail(suscriptor, f"El juego {game} ha bajado de precio a {price}€.")


#class MockDataBase():
#    def getAllSuscritors(self, game):
#        return ["pepe@gmail.com", "secon@gmail.com"]
    
#class MockMailClient():
#    def send_mail(self, user, message):
#        pass

#ActionAlertWhenPriceIsCheaper(MockDataBase(), MockMailClient()).Execute("Cyberpunk 2077", 50)

#MockMailClient.send_mail.assert_called_with("pepe@gmail.com", "El juego Cyberpunk 2077 ha bajado de precio 50€")
#MockMailClient.send_mail.assert_called_with("secon@gmail.com", "El juego Cyberpunk 2077 ha bajado de precio 50€")
