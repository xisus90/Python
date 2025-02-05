from data_code import ActionGetPrice
from data_code import SuscriptionsMenu

class users():
     
    def user_search(self, mail):

        try:
            game = input("Escribe el nombre del juego que deseas buscar: ").strip()

            if not game:  # Si el usuario no escribe nada
                raise ValueError("No se ha escrito nada en el valor nombre")

            game_info = ActionGetPrice().Execute(game)  # Busca el juego

            if game_info:
                game_name, game_price = game_info  # Desempaquetar la tupla
                print(f"El juego es {game_name} y tiene un precio de {game_price}€")
            else:
                print("No se encontró el juego.")

        except ValueError as e:
            print(e)

        try:
            option = input(f"¿Deseas suscribirte al juego? ")
            if not option:  # Si el usuario no escribe nada
                raise ValueError("No se ha escrito nada en el valor")
            
            if option == "si":
                games = SuscriptionsMenu().suscriptorgames(mail)
                if games == game:
                    print("Ya estas suscrito a ese juego")
                if games != game:
                    SuscriptionsMenu().suscription(mail, game)
                
            if option == "no":
                print(f"Gracias por usar nuestro buscador, esperamos verle pronto.")     
        except ValueError as e:
            print (e)

        
    def user(self):
        
        mail = input (f"introduce tu correo electronico:").strip()
        gamesinfo = SuscriptionsMenu().suscriptorgames(mail)
        
        if gamesinfo:
        
            for game in gamesinfo:
                game_name, game_price = ActionGetPrice().Execute(game)  # Desempaquetar la tupla
                print(f"Estás suscrito al juego {game_name}: {game_price}€")
                
            try:
                option = input(f"¿Deseas buscar otro juego? ")
                if not option:  # Si el usuario no escribe nada
                    raise ValueError("No se ha escrito nada en el valor")
                if option == "si":
                    self.user_search(mail) 
                if option == "no":
                    print(f"Gracias por usar nuestro buscador, esperamos verle pronto.")
                    exit()   
            except ValueError as e:
                print (e)
                exit()
        else:
            print("el juego no estas suscrito a ningún juego")
              
class Notuser():

    def searchgames(self):

        try:
            game = input("Escribe el nombre del juego que deseas buscar: ").strip()

            if not game:  # Si el usuario no escribe nada
                raise ValueError("No se ha escrito nada en el valor nombre")

            game_info = ActionGetPrice().Execute(game)  # Busca el juego

            if game_info:
                game_name, game_price = game_info  # Desempaquetar la tupla
                print(f"El juego es {game_name} y tiene un precio de {game_price}€")
            else:
                print("No se encontró el juego.")

        except ValueError as e:
            print(e)

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
            SuscriptionsMenu().suscription( Usermail, game_name)
        
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
 

Menu().execute()
