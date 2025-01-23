from data_code import datas_games
from data_code import Database 
from data_code import Suscription

class users():
     
    def user_search(self, name, mail):

        try:
            game = input(f"¿Escribe el nombre del juego que deseas buscar? ")
            gameprice = Database().findprice(game)
        except ValueError:
                    print("No se ha escrito nada en el valor nombre")
        print (f"el juego es {game} tiene un precio de {gameprice}€")

        while True:
            try:
                option = input(f"¿Deseas suscribirte al juego? ")

                if not option.strip():  # Si no se escribe nada (cadena vacía o solo espacios)
                    raise ValueError("No se ha escrito nada. Por favor, introduce si o no.")
                
                if option == "si":
                     Suscription().suscription(name, mail, game)
                  
                if option == "no":
                    print(f"Gracias por usar nuestro buscador, esperamos verle pronto.")
                    break       
            except ValueError as error:
                print (error)

        
    def user(self):
        
        name = input (f"introduce tu nombre:")
        mail = input (f"introduce tu correo electronico:")
        games = Suscription().suscriptorgames(name)
        gameprice = Database().findprice(games)
        
        print (f"el juego al que estas suscrito es {games} con un precio de {gameprice}€")
        while True:
            try:
                option = input(f"¿Deseas buscar otro juego? ")

                if not option.strip():  # Si no se escribe nada (cadena vacía o solo espacios)
                    raise ValueError("No se ha escrito nada. Por favor, introduce si o no.")
                
                if option == "si":
                    self.user_search(name, mail)
                    break 
                if option == "no":
                    print(f"Gracias por usar nuestro buscador, esperamos verle pronto.")
                    break       
            except ValueError as error:
                print (error)

              
class Notuser():

    def searchgames(self):

        try:
            game_to_find = input("introduce el juego que deseas buscar: ")
        except ValueError:
            print(f"Debes escribir algo en este campo")
            exit()

        pricegame = datas_games().gamesforuser(game_to_find)
        
        print(f"el precio del juego {game_to_find} es de {pricegame}€\n")

        try:
            selection = input(f"¿deseas suscribirte Se te notificará cuando bajen el precio de los juegos que deseas\n")
        except ValueError:
            print(f"escribe el parametro correctamente")
            exit()

        if selection == "si":
            try:
                Username = input(f"Introduce tu nombre de usuario: ")
            except ValueError:
                    print("No se ha escrito nada en el valor nombre")
                    exit()
            try:
                Usermail = input(f"Introduce tu correo electronico: ") 
            except ValueError:
                print("No se ha escrito nada en el valor del email")
                exit()
            Suscription().suscription(Username, Usermail, game_to_find)
        
        if selection == "no":
            print("Gracias por usar el nuestro buscador.")


class Menu():
     
    def chechking(self):


        checking = input (f"Estas suscrito? ")           

        if checking == "si":
            users().user()

        if checking == "no":
            Notuser().searchgames()

        if checking != "si" and checking != "no":
            print ("No se puede dejar el campo en blanco o no se ha escrito correctamente.")
 

        #try:
        #    selection = input(f"¿deseas crear una tabla con todos los juegos por precios y fecha?\n")
        #    if selection == "si":
        #        Database().grafic()
        #    if selection != "si":
        #        exit()
        #except ValueError:
        #    exit()

Menu().chechking()
