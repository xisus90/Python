from scraper_code import SearchGame

game_to_find = input("introduce el juego que deseas buscar: ")
platform = input("Introduce la plataforma del juego que deseas: ")

pricegame = SearchGame(game_to_find, platform).search()

print(f"el enlace de la plataforma {platform} es: {pricegame} ")