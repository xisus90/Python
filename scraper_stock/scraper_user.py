from data_code import datas_games


game_to_find = input("introduce el juego que deseas buscar: ")


pricegame = datas_games().gamesforuser(game_to_find)

print(f"el juego {game_to_find} tiene un precio de {pricegame}€")