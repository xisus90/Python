import requests


API_URL = "http://127.0.0.1:5000"

class Menu:
    
    def __init__(self):
        self.api_url = API_URL

    def login(self, account):
        login = requests.post(f"{self.api_url}/login_user", json={"account": str(account)})

        if login.status_code != 200:
            print(f"Error: {login.status_code} - {login.text}")  # Manejo de errores
        if login.status_code == 200:
            data = login.json()

            games = data.get('games')  

            if games:
                return games
                print(f"{games} ")
            else:
                print("No se encontraron juegos asociados a este correo.")


    def search(self, game):
        
        search = requests.post(f"{self.api_url}/search_game", json={"game": str(game)})
                            
        if search.status_code != 200:
            print(f"Error: {search.status_code} - {search.text}")  # Manejo de errores   

        if search.status_code == 200:
            data = search.json() 
            game_name = data.get('GameName')
            game_price = data.get('GamePrice')
            print(f"{game_name}: {game_price}€\n")


    def register(self, email):

        register = requests.post(f"{self.api_url}/register_user", json={"email": str(email), "game" : str(game_name)})
        data = register.json()
        acction = data.get('message')
        print(acction)


    print (f"")

    def show_menu(self):

        print("\n--- MENÚ DE USUARIOS ---")
        print(f"1: Iniciar sesión")
        print(f"2: Buscar un juego")
        print(f"3: Salir")


        while True:

            try:
                option = int(input("Selecciona una opción (1-3): "))
            except ValueError:
                print("❌ Entrada no válida. Ingresa un número entre 1 y 3.")
                continue

            if option not in [1, 2, 3]:
                print("❌ Opción no válida. Intenta de nuevo.")
                continue

            if option == 1:
                account = input("Introduce tu correo electronico: ")
                games_user = self.login(account)
                for game in games_user:    
                    prices_games_user = self.search(game)
                    print (f"Estas suscrito a {game} {prices_games_user}€")
                    break

            if option == 2:
                game = input("Introduce el juego que deseas buscar:\n")
                search_game = self.search(game)
                print ("""Al registrarte como usuario podrás recibir notificaciones de la bajada de precios de los juegos a los que estas suscrito""")
                select = input("Deseas suscribirte?(si/no):")

                if select == "si":
                    email = input("Introduce un correo electrónico: ")
                    self.register(email)

                if select == "no":
                    print ("Gracias por usar nuestro buscador")
                    break

            if option == 3:
                print(" Saliendo del programa. ¡Hasta luego!")
                break


if __name__ == "__main__":
    Menu().show_menu()
