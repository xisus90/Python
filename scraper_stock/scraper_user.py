from data_code import ActionGetPrice
from data_code import Database 
from data_code import SuscriptionsMenu

class users():
     
    def user_search(self, mail):

        try:
            game = input(f"¿Escribe el nombre del juego que deseas buscar? ")
            gameprice = Database().findprice(game)
        except ValueError:
                    print("No se ha escrito nada en el valor nombre")
        print (f"el juego es {game} tiene un precio de {gameprice}€")

        while True:
            try:
                option = input(f"¿Deseas suscribirte al juego? ")

                if option == "si":
                    games = SuscriptionsMenu().suscriptorgames(mail)
                    if games == game:
                        print("Ya estas suscrito a ese juego")
                    if games != game:
                        Database().update_db_user(mail, game)
                  
                if option == "no":
                    print(f"Gracias por usar nuestro buscador, esperamos verle pronto.")     
            except ValueError:
                print ("error el campo está vacio")

        
    def user(self):
        
        mail = input (f"introduce tu correo electronico:").strip()
        games = SuscriptionsMenu().suscriptorgames(mail)

        if games:
            
            for game in games:
                gameprices = ActionGetPrice().Execute(game)
                print(f"Estas suscrito al juego {game}: {gameprices}€")

            try:
                option = input(f"¿Deseas buscar otro juego? ")
                if option == "si":
                    self.user_search(mail) 
                if option == "no":
                    print(f"Gracias por usar nuestro buscador, esperamos verle pronto.")   
            except ValueError:
                print ("error campo vacio")
                exit()
        else:
            print("el juego no estas suscrito a ningún juego")
              
class Notuser():

    def searchgames(self):

        try:
            game_to_find = input("introduce el juego que deseas buscar: ")
        except ValueError:
            print(f"Debes escribir algo en este campo")
            exit()

        pricegame = ActionGetPrice().Execute(game_to_find)
        
        print(f"el precio del juego {game_to_find} es de {pricegame}€\n")

        try:
            selection = input(f"¿deseas suscribirte Se te notificará cuando bajen el precio de los juegos que deseas\n")
        except ValueError:
            print(f"escribe el parametro correctamente")
            exit()

        if selection == "si":
            try:
                Usermail = input(f"Introduce tu correo electronico: ") 
            except ValueError:
                print("No se ha escrito nada en el valor del email")
                exit()
            SuscriptionsMenu().suscription( Usermail, game_to_find)
        
        if selection == "no":
            print("Gracias por usar el nuestro buscador.")


class Menu():
     
    def execute(self):


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


Menu().execute()
