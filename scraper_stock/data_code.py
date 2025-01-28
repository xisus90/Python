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

        self._cursor.close()
        self._connection.close()

        if result:
            return result[0] 
        else:
            print("El juego que buscas no existe")
            exit()


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


    def checking_user(self, user, mail):
    
        user = user.strip().lower()
        mail = mail.strip().lower()
        
        
        self._cursor.execute("""SELECT NameUser, EmailUser FROM users WHERE 
                            NameUser = %s AND EmailUser = %s""", (user, mail,))
        both_exists = self._cursor.fetchone()

        self._cursor.execute("SELECT NameUser FROM users WHERE NameUser = %s", (user,))
        user_exists = self._cursor.fetchone()

        self._cursor.execute("SELECT EmailUser FROM users WHERE EmailUser = %s", (mail,))
        mail_exists = self._cursor.fetchone()

        self._cursor.close()
        self._connection.close()
        
        if both_exists:
            print("existen ambos")
            return "both_exist"
        if user_exists and not mail_exists:
            return "user_exist"  
        if mail_exists and not user_exists:
            return "mail_exist"
        return "not_exist"


    def new_user(self, user, mail, game):

        check = self.checking_user(user, mail)

        if check == "not_exist":    
            self._cursor.execute("""INSERT IGNORE INTO users (NameUser, EmailUser, GameName)
                                    VALUES (%s, %s, %s)""", (user, mail, game))
            self._connection.commit()
            
            print(f"has sido registrado correctamente\n")

            self._cursor.close()
            self._connection.close()

        if check == "both_exist":
            print(f"El nombre de usuario y mail ya existen")
        if check == "user_exist":
            print(f"El nombre de usuario ya existe")
        if check == "mail_exist":
            print(f"El mail de usuario ya existe")


    def get_game_for_user(self, user):
        
            user = user.strip().lower()
            self._cursor.execute("SELECT GameName FROM users WHERE NameUser = %s", (user,))
            result = self._cursor.fetchone()

            self._cursor.close()
            self._connection.close()

            if result:
                return result[0] 
            else:
                print("El juego que buscas no existe")
                exit()
    
    
    def user_to_game(self, game):

        game = game.strip().lower()
        self._cursor.execute("SELECT NameUser FROM users WHERE GameName LIKE %s", (f"%{game}%",))
        results = self._cursor.fetchall()
        self._cursor.close()
        self._connection.close()

        if results:
            return results[0]


    def update_db_user(self, user, mail, game):

        update = """
        UPDATE users
        SET GameName = CONCAT(GameName, ', ', %s)
        WHERE NameUser = %s AND EmailUser = %s
             """
        
        self._cursor.execute(update, (game, user, mail))
        self._connection.commit() 
        print(f"Juego añadido correctamente al usuario {user}.")


class Suscription:


    def suscription(self, user, mail, game):
        
        Database().new_user(user, mail, game)
  
    
    def suscriptorgames(self, user, mail):
        
        check = Database().checking_user( user, mail)

        if check == "both_exist":
            print("Obteniendo juegos...")
            gamename = Database().get_game_for_user(user)  # Supongamos que esta función ya existe
            return gamename
        if check == "user_exist" or check == "mail_exist" or check == "not_exist":
            print("nombre de usuario o email incorrectos.")
            exit()


class datas_games:


    def pricegames(self, game):

        gameprice = Database().findprice(game)
        return gameprice

