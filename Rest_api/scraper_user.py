import requests

API_URL = "http://127.0.0.1:5000"

class Menu:
    def show_menu(self):
        try:
            response = requests.get(f"{API_URL}/usuarios")
            menu_opciones = response.json()

            while True:
                print("\n--- MENÚ DE USUARIOS ---")
                for key, value in menu_opciones.items():
                    print(f"{key}. {value}")

                option = int(input("Selecciona una opción (1-3): "))

                if option != 1 and option != 2 and option != 3:
                    print("❌ Opción no válida. Intenta de nuevo.")
                if 1 <= option <= 3:
                    return option

        except requests.RequestException as e:
            print(f"Error al conectar con la API: {e}")

if __name__ == "__main__":
    Menu().show_menu()