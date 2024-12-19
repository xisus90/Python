from brawl_maps import mapsforbrawler


try:
   Brawler = input("Introduce el Brawler que deseas saber en que mapa funciona correctamente ")
except ValueError:
    print("El campo del peso no está definido o es inválido.")
    exit()



brawler_maps = mapsforbrawler(Brawler).execute()

print(f"El {Brawler} es bueno en los mapas:")