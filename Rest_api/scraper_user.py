import requests


API_URL = "http://127.0.0.1:5000"

class Menu:

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

                acount = input("Introduce tu correo electronico:")
                response = requests.post(f"{API_URL}/login_user", json = {"acount": str(acount)} )
                #result = requests.get(f"{API_URL}/search_game" , params = {""})

                print ("""Al registrarte como usuario podrás recibir notificaciones de la bajada 
                       de precios de los juegos a los que estas suscrito""")
                email = input("Introduce un correo electrónico: ")
                response = requests.post(f"{API_URL}/register_user", json={"email": str(email)})
  

            if option == 2:
              game = input("Introduce el juego que deseas buscar:\n")
            response = requests.post(f"{API_URL}/search_game", json={"game": str(game)})

            if response.status_code == 200:
                data = response.json() 
                game_name = data.get('GameName')
                game_price = data('GamePrice')
                print(f"{game_name}: {game_price}€")
            else:
                print(f"Error: {response.status_code} - {response.text}")  # Manejo de errores


            if option == 3:
                print (f"gracias por usar nuestro buscador")

            else:
                print(f"⚠️ Error en la respuesta del servidor: {response.status_code}")

            if option == 3:
                print(" Saliendo del programa. ¡Hasta luego!")
                break


if __name__ == "__main__":
    Menu().show_menu()
