from flask import Flask, jsonify, request

app = Flask(__name__)

# 🗂️ Menú de opciones
@app.route('/usuarios', methods=['GET'])
def obtener_menu():
    menu_opciones = {
        "1": "Registrar usuario",
        "2": "Buscar juego",
        "3": "Salir"
    }
    return jsonify(menu_opciones)

# ✅ Procesar la opción seleccionada
@app.route('/procesar_opcion', methods=['POST'])
def procesar_opcion():
    data = request.json
    opcion = data.get("opcion")

    if opcion == "1":
        print("Has seleccionado registrar un usuario.")
        return jsonify({"mensaje": "Has seleccionado registrar un usuario."})
    if opcion == "2":
        print("Has seleccionado buscar un juego.")
        return jsonify({"mensaje": "🎮 Has seleccionado buscar un juego."})
    if opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        return jsonify({"mensaje": "🚪 Saliendo del programa. ¡Hasta luego!"})

    # Manejo de error si la opción es inválida
    return jsonify({"error": "Opción inválida"}), 400

if __name__ == "__main__":
    app.run(debug=True)

