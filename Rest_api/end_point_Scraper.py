import requests
from flask import Flask, jsonify, request
from Database import DB_Usergames

app = Flask(__name__)


@app.route('/register_user', methods=['POST'])
def register():
    data = request.json
    email = data.get("email")
    
    if not email:
        return jsonify({"error": "Faltan parámetros."}), 400
    
    db = DB_Usergames()
    db.new_user(email)

    return jsonify({"message": "Usuario registrado con éxito!"}), 200


@app.route('/login_user', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    
    if not email:
        return jsonify({"error": "Faltan parámetros."}), 400
    
    db = DB_Usergames()
    resultgames = db.get_game_for_user(email)
    
    if resultgames:
        resultgames = resultgames.get_json()  # Esto extrae la lista de juegos del objeto jsonify

    for result in resultgames:
        resultprices = db.getprice(result)
        game_name = resultprices['GameName']
        game_price = resultprices['GamePrice']
        print(f"Estas suscrito al juego {game_name}: {game_price}€")


@app.route('/search_game', methods=['POST'])
def search():
    data = request.json
    game = data.get("game")
    
    if not game:
        return jsonify({"error": "Faltan parámetros."}), 400
    
    db = DB_Usergames()  
    getpriceforgame = db.getprice(game)

    if not getpriceforgame or not isinstance(getpriceforgame, dict):
        return jsonify({"error": "Juego no encontrado o error en la consulta."}), 404

    game_name = getpriceforgame.get("GameName")  # Usamos .get() para evitar KeyError
    game_price = getpriceforgame.get("GamePrice")

    return jsonify({"GameName": game_name, "GamePrice": game_price})



if __name__ == "__main__":
    app.run(debug=True)

