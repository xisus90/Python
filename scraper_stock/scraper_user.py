from data_code import datas_games
from data_code import Database 
from data_code import Suscription

class users():
     
     def user(self):
        
        name = input (f"introduce tu nombre:")
        games = Suscription().suscriptorgames(name)
        
        print (f"el juego al que estas suscrito es {games} ")


class Notuser():

    def searchgames(self):

        try:
            game_to_find = input("introduce el juego que deseas buscar: ")
        except ValueError:
            print(f"El juego que buscas no existe o está mal escrito")
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
