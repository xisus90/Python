import requests
from flask import Flask, jsonify, request
from Database import DB_Usergames
import json

app = Flask(__name__)


@app.route('/register_user', methods=['POST'])
def register():

    data = request.json
    email = data.get("email")
    game = data.get("game")
    
    if not email:
        return jsonify({"error": "Faltan parámetros."}), 400
    
    db = DB_Usergames()
    db.new_user(email, game)

    return jsonify({"message": "Usuario registrado con éxito!"}), 200


@app.route('/login_user', methods=['POST'])
def login():
    data = request.json
    account = data.get("account")
    
    if not account:
        return jsonify({"error": "Faltan parámetros."}), 400
    
    db = DB_Usergames()
    resultgames = db.get_game_for_user(account)
    
    # Aquí, ya no necesitas llamar a get_json() porque 'resultgames' ya está en formato JSON
    if resultgames:  
        # Procesa los juegos desde 'resultgames' que es una lista de diccionarios
        games = [game["GameName"] for game in resultgames]

        # Devuelve la respuesta con los juegos como JSON
        return jsonify({"games": games})

    # Si no hay juegos o ocurre algún error, también necesitas devolver una respuesta
    return jsonify({"error": "No games found"}), 400




@app.route('/search_game', methods=['POST'])
def search():
    data = request.json
    game = data.get("game")
    
    if not game:
        return jsonify({"error": "Faltan parámetros."}), 400

    db = DB_Usergames()  
    getpriceforgame = db.getprice(game)

    game_data = getpriceforgame.get_json()

    if not game_data or not isinstance(game_data, dict):
        return jsonify({"error": "Juego no encontrado o error en la consulta."}), 404

    game_name = game_data.get("GameName")  # Usamos .get() para evitar KeyError
    game_price = game_data.get("GamePrice")

    return jsonify({"GameName": game_name, "GamePrice": game_price})



if __name__ == "__main__":
    app.run(debug=True)

