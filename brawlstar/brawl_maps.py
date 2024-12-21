from dataclasses import dataclass
@dataclass 


class mapsforbrawler:
 
    def __init__(self, brawler):       
            self._brawler = brawler


    def execute(self):
        brawl_maps = BrawlSearch(self._brawler).brawlersList()
        return brawl_maps    



class BrawlSearch:
    
    def __init__(self, brawler):
            self._brawler = brawler
    
    def brawlersList(self):
        brawlerList = ["Penny", "Pam", "Crow", "Leo", "Ivy"]
        position = 0
        while position <= (len(brawlerList)):
            if brawlerList[position] == self._brawler :
                goodmap = MapSearch(brawlerList[position]).MapList()
                return goodmap
            position += 1



class MapSearch:

    def __init__(self, brawlerList):
        self._brawlerList = brawlerList

    def MapList(self):
        
        maplist= {
                "Penny": "Mina rocosa, Arcade de cristal, Espacio abierto",
                "Pam": "Brrumm Brrumm, Ultima parada",
                "Crow": "Claro del bosque, Avalancha Rocosa",
                "Leo":"Pradera traicionera, Escondite",
                "Ivy":"Canal grande, Crimen organizado"          
               }
        brawl_map = maplist[self._brawlerList]
             
        return brawl_map

        


