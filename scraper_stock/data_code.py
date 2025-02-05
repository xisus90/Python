import pymysql
import csv
from typing import Optional, Any

class Database_UserGames:
    
    def __init__(self):

        """Inicializa la conexión a la base de datos."""
        self._connection = pymysql.connect(
            host="localhost", 
            user="root",
            password="root",
            db="gamelist"
        )
        self._cursor = self._connection.cursor()


    def close(self):

        """Cierra la conexión y el cursor de manera segura."""
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()
        print("Conexión cerrada correctamente.")


    def __del__(self):

        """Asegura que la conexión se cierre cuando el objeto sea eliminado."""
        self.close()


    def execute_query(self, query: str, params: tuple = (), fetch_one=False, fetch_all=False) -> Any:

        """Ejecuta una consulta de manera segura y devuelve los resultados si es necesario."""
        try:
            self._cursor.execute(query, params)
            if fetch_one:
                return self._cursor.fetchone()
            if fetch_all:
                return self._cursor.fetchall()
            self._connection.commit()  # Para INSERT, UPDATE, DELETE
            return None
        except pymysql.MySQLError as e:
            print(f"Error en la consulta SQL: {e}")
            return None


    def findprice(self, game: str) -> Optional[float]:

        """Busca el precio de un juego."""
        result = self.execute_query(
            "SELECT Gamesnames, Gamesprices FROM games WHERE Gamesnames LIKE  %s", (f"%{game}%",), fetch_one=True
        )
        return result if result else None

  
    def new_user(self, mail: str, game: str):

        """Registra usuario si no existe."""

        self.execute_query(
            "INSERT INTO users (EmailUser, GameName) VALUES (%s, %s)", (mail, game)
        )
        print("Usuario suscrito correctamente.")


    def get_game_for_user(self, mail: str):

        """Obtiene todos los juegos asociados a un correo."""
        results = self.execute_query(
            "SELECT GameName FROM users WHERE EmailUser = %s", (mail,), fetch_all=True
        )
        return [result[0] for result in results] if results else None


    def get_mail_for_game(self, game: str):

        """Obtiene todos los juegos asociados a un correo."""
        results = self.execute_query(
            "SELECT EmailUser FROM users WHERE GameName = %s", (game,), fetch_all=True
        )
        return [result[0] for result in results] if results else None



    def user_to_game(self, game: str):

        """Obtiene todos los usuarios suscritos a un juego."""
        results = self.execute_query(
            "SELECT EmailUser FROM users WHERE GameName = %s", (game,), fetch_all=True
        )
        return [result[0] for result in results] if results else None


    #def update_db_user(self, mail: str, game: str):

    #    """Añade un juego a la lista de juegos de un usuario."""
    #

    #    self.execute_query(
    #        """UPDATE users
    #           SET GameName = CONCAT(GameName, ', ', %s)
    #           WHERE EmailUser = %s""",
    #        (game, mail)
    #    )
    #    print(f"Juego añadido correctamente al usuario {mail}.")

# ------------------- CLASES QUE USAN DATABASE -------------------

class SuscriptionsMenu:

    def __init__(self):
        self._data = Database_UserGames()

    def suscriptorgames(self, mail: str):

        """Devuelve todos los juegos suscritos por un usuario."""
        return self._data.get_game_for_user(mail)


    def check_is_user_already_have_game(self, mail: str, game: str):

        """Comprueba que el usuario no se suscriba a un juego que ya está suscrito"""
        check_user_games = self.suscriptorgames(mail)
        
        for games in check_user_games:
            if games == game:
                print("Ya estas suscrito a este juego")
                exit()


    def check_max_suscriptions(self, mails: str):

        """Comprueva la cantidad de veces que está suscrita el usuario ya que tiene un tope de 5 subs"""
        maxsubs  = self.suscriptorgames(mails)
        
        if len(maxsubs) >= 5:
            print ("Has superado el máximo de suscripciones")
            print (f"{len(maxsubs)}")
            exit()
        if not maxsubs:  # Si el usuario no tiene juegos, maxsubs será None
            return False  # Puede seguir suscribiéndose


    def suscription(self, mail: str, game: str):

        """Añade una suscripción de usuario a un juego."""
        self.check_max_suscriptions(mail)
        self.check_is_user_already_have_game(mail, game)
        self._data.new_user(mail, game)



class ActionGetPrice:

    def __init__(self):
        self._data = Database_UserGames()


    def Execute(self, game: str) -> Optional[float]:

        """Obtiene el precio de un juego."""
        return self._data.findprice(game)
    



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
