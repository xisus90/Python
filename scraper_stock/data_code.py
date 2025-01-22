import pymysql
import csv

class Database:
    
    def __init__(self):
        
        self._connection = pymysql.connect(
        host="localhost", 
        user="root",
        password="root",
        db="gamelist"
        )
        
        self._cursor = self._connection.cursor()


    def findprice(self, game):
        
        self._cursor.execute("SELECT Gamesprices FROM games WHERE Gamesnames = %s", (game))
        result = self._cursor.fetchone()

        if result:
            return result[0]  # Devuelve el valor del precio (primera columna)
        else:
            print("El juego que buscas no existe")
            exit()
        
        self._cursor.close()
        self._connection.close()


    def grafic(self):

        self._cursor.execute("SELECT Gamesnames, Gamesprices, Date From games")
        result = self._cursor.fetchall()
        
        with open("exported_data.csv", mode="w", newline="") as datafile:
            writer = csv.writer(datafile)
        
            writer.writerow(["Gamesnames", "Gamesprices", "Date"])
        
            for fila in result:
             writer.writerow(fila)
    
        print("Datos exportados correctamente a 'exported_data.csv'")
            

        self._cursor.close()
        self._connection.close()


class datas_games:

    def gamesforuser(self, game):

        gameprice = Database().findprice(game)
        return gameprice
