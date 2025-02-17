import requests
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


@app.route('/register_user', methods=['POST'])
def register_users():
    data = request.json
    email = data.get("email")
    
    if not email:
            return jsonify({"error": "El nombre de usuario y el correo electrónico son obligatorios."}), 400

    print(f"Registrando el email: {email}")

    return jsonify({f" El mail {email} ha sido registrado correctamente!"}), 200

if __name__ == "__main__":
    app.run(debug=True)

