from data_code import datas_games
from data_code import Database

game_to_find = input("introduce el juego que deseas buscar: ")


pricegame = datas_games().gamesforuser(game_to_find)

print(f"el juego {game_to_find} tiene un precio de {pricegame}€")

try:
    selection = input(f"¿deseas crear una tabla con todos los juegos por precios y fecha?\n")
    if selection == "si":
        Database().grafic()
    if selection == "no":
        exit()
except ValueError:
    exit()

