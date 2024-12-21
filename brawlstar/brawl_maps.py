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
                goodmap = MapSearch(brawlerList[position], position).MapList()
                return goodmap
            position += 1



class MapSearch:

    def __init__(self, brawlerList, position):
        self._brawlerList = brawlerList
        self._position = position

    def MapList(self):
        
        print(f"el brwaler {self._brawlerList} está en la posición {self._position} de la array")
        prueba = "todo ok"
        return prueba
        


