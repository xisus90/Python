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
        print(f" Has seleccionado registrar un usuario.")
        return jsonify({" Has seleccionado registrar un usuario."})
    if opcion == "2":
        print()
        return jsonify({"🎮 Has seleccionado buscar un juego."})
    if opcion == "3":
        return jsonify({"🚪 Saliendo del programa. ¡Hasta luego!"})


if __name__ == '__main__':
    app.run(debug=True)