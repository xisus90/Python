import pymysql
import csv
from typing import Optional, Any
from pymysql.cursors import DictCursor
from flask import jsonify



class DB_Usergames:
    
    def __init__(self):

        """Inicializa la conexión a la base de datos."""
        self._connection = pymysql.connect(
            host ="localhost", 
            user ="root",
            password ="root",
            db ="usergames",
            cursorclass = DictCursor
        )
        self._cursor = self._connection.cursor()


    def close(self):

        """Cierra la conexión y el cursor de manera segura."""
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()
 


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


    def getprice(self, game: str) -> Optional[float]:

        """Busca el precio de un juego."""
        result = self.execute_query(
            "SELECT Gamesnames, Gamesprices FROM games WHERE Gamesnames LIKE  %s", (f"%{game}%",), fetch_one=True
        )
        
        if result:
            return jsonify({"GameName": result['Gamesnames'], "GamePrice": result['Gamesprices']})
        else:
            return jsonify([])

  
    def new_user(self, mail: str, game: str):

        """Registra usuario si no existe."""

        self.execute_query(
            "INSERT INTO users (EmailUser, GameName) VALUES (%s, %s)", (mail, game)
        )

  
    def get_game_for_user(self, mail: str):
        """Obtiene todos los juegos asociados a un correo."""
        results = self.execute_query(
            "SELECT GameName FROM users WHERE EmailUser = %s", (mail,), fetch_all=True
        )

        if results:
            # Aquí devuelve directamente la lista de resultados, no un Response
            return [{"GameName": result["GameName"]} for result in results]  # Devuelve una lista de diccionarios
        else:
            return []  # Si no hay resultados, devuelve una lista vacía


    def get_mail_for_game(self, game: str):
        """Obtiene todos los correos electrónicos asociados a un juego."""
        results = self.execute_query(
            "SELECT EmailUser FROM users WHERE GameName = %s", (game,), fetch_all=True
        )
        
        print(results)
 
        if results:
            return jsonify([result['EmailUser'] for result in results])
        else:
            return jsonify([])


    def user_suscribed_game(self, game: str):

        """Obtiene todos los usuarios suscritos a un juego."""
        results = self.execute_query(
            "SELECT EmailUser FROM users WHERE GameName = %s", (game,), fetch_all=True
        )  
        
        if results:
            return jsonify([result['EmailUser'] for result in results])
        else:
            return jsonify([])

