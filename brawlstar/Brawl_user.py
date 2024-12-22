from brawl_maps import mapsforbrawler


Brawler = input("Introduce un Brawler y se imprimiran sus mejores mapas: ")




brawler_maps = mapsforbrawler(Brawler).execute()

print(f"El {Brawler} es bueno en los mapas: {brawler_maps}")