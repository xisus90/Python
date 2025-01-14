from scraper_code import SearchGame

game_to_find = input("introduce el juego que deseas buscar: ")
platform = input("Introduce la plataforma del juego que deseas:\n Battle.net\n Epic Games\n GoG.com\n Microsoft Store\n Nintendo Eshop\n Ea App\n PlayStation Store\n RockStar\n Steam\n Ubisoft:\n")


pricegame = SearchGame(game_to_find, platform).search()

print(f"{pricegame} ")
