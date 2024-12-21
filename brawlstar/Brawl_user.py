from brawl_maps import mapsforbrawler


try:
   Brawler = input("Introduce un Brawler y se imprimiran sus mejores mapas: ")
except ValueError:
    print("El campo del peso no está definido o es inválido.")
    exit()



brawler_maps = mapsforbrawler(Brawler).execute()

print(f"El {Brawler} es bueno en los mapas: {brawler_maps}")