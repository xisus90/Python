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

                try:
                    option = int(input("Selecciona una opción (1-3): "))
                except ValueError:
                    print("❌ Entrada no válida. Ingresa un número entre 1 y 3.")
                    continue

                if option not in [1, 2, 3]:
                    print("❌ Opción no válida. Intenta de nuevo.")
                    continue

                # Enviar la opción al servidor y manejar la respuesta
                response = requests.post(f"{API_URL}/procesar_opcion", json={"opcion": str(option)})

                if response.status_code == 200:
                    print(response.json())  # Ahora imprimirá {"mensaje": "Has seleccionado registrar un usuario."}
                else:
                    print(f"⚠️ Error en la respuesta del servidor: {response.status_code}")

                # Si el usuario elige la opción 3, salir del bucle
                if option == 3:
                    print(" Saliendo del programa. ¡Hasta luego!")
                    break

        except requests.RequestException as e:
            print(f"❌ Error al conectar con la API: {e}")

if __name__ == "__main__":
    Menu().show_menu()
