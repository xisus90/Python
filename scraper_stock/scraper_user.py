from data_code import datas_games


game_to_find = input("introduce el juego que deseas buscar: ")


pricegame = datas_games().gamesforuser(game_to_find)

print(f"el juego {game_to_find} tiene un precio de {pricegame}€")

try:
    selection = input(f"¿Deseas comparar el precio del juego{game_to_find} con el precio anterior?")
except ValueError:
    exit()

if selection == "si":
    comparepricegame = datas_games().compareprices(game_to_find)
    print (f"el precio más antiguo registrado es de {comparepricegame}€ respecto al actual que es de {pricegame}€")
if selection == "no":
    exit()