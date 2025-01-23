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

        print(result)

        if result:
            return result[0] 
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


    def user_db(self, user, mail, game):

        
        self._cursor.execute("""INSERT IGNORE INTO users (NameUser, EmailUser, GameName)
                                 VALUES (%s, %s, %s)""", (user, mail, game))
        self._connection.commit()
        
        print(f"has sido registrado correctamente\n")

        self._cursor.close()
        self._connection.close()

    def get_game_for_user(self, user):
        
        user = user.strip().lower()
        self._cursor.execute("SELECT GameName FROM users WHERE NameUser = %s", (user,))
        result = self._cursor.fetchone()

        print(result) # esto me devuelve el nombre sin tratar como ('Atomfall',)


        if result:
            return result[0] #esto me devuelve None
        else:
            print("El juego que buscas no existe")
            exit()
  
        self._cursor.close()
        self._connection.close()


class Suscription():

    def suscription(self, user, mail, game):
        
        Database().user_db(user, mail, game)
        return
    
    def suscriptorgames(self, name):

        Database().get_game_for_user(name)



class datas_games:

    def gamesforuser(self, game):

        gameprice = Database().findprice(game)
        return gameprice
