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

        if result:
            return result[0] 
        else:
            print("El juego que buscas no existe")
            exit()
  
        self._cursor.close()
        self._connection.close()


class Suscription:

    def suscription(self, user, mail, game):
        
        #para mañana hacer una función que se encargue de mostrar solo los juegos de los subscritos
        #hacer otra función que se encargue de comprobar si estas registrado y si no lo estas
        #subscribirte y una tercera que se encargue de actualizar los datos de una tabla si estas en
        # la db, para colocar el nuevo juego al que te has subscrito
        # y en scraper_code que llame a este documento y mande un correo a la persona cuando compruebe
        #que un juego ha bajado de precio
        #modificar en el user, cuando te dice que te suscribas por primera vez y la funcion nueva se
        #llame newuser, la de buscar en la db, searchdb o similar, y la de actualizar updateuserdb
        Database().user_db(user, mail, game)
        Database().user_update(game)
    
    def suscriptorgames(self, name):

        gamename = Database().get_game_for_user(name)
        return gamename


class datas_games:

    def gamesforuser(self, game):

        gameprice = Database().findprice(game)
        return gameprice
