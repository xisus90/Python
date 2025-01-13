import re
from dataclasses import dataclass
import requests
@dataclass
 


class mapsforbrawler:
 
    def __init__(self, brawler):       
            self._brawler = brawler


    def execute(self):
        #brawler_Memory_exists = BrawlersDataMemory().exists(self._brawler)
        #if not brawler_Memory_exists:
        #return "No existe brawler en data memory"
        brawler_Web_exists = BrawlersDataWeb().exists(self._brawler)
        if not brawler_Web_exists:
            return "No existe brawler en data memory"

        goodmap = MapSearch(self._brawler).MapList()
        return goodmap    


class BrawlersDataMemory:
    
    def __init__(self):
        self._brawlerList = ["Penny", "Pam", "Crow", "Leo", "Ivy"]

    def get_brawlers(self):
        return self._brawlerList

    def exists(self, brawler):
        return brawler in self._brawlerList


class BrawlersDataWeb:
    
    def __init__(self):
        data_url = "https://brawlify.com/es/brawlers/"
        result = requests.get(data_url)
        content = result.text
        data_sequence = r'h6 mb-0">(.*?)</h2>'
        datas = re.findall(data_sequence, str(content))

        self._data_brawlers = []

        for i in datas:
            self._data_brawlers.append(i)
            

    def get_brawlers(self):
        return self._data_brawlers

    def exists(self, brawler):
        return brawler in self._data_brawlers


class MapSearch:

    def __init__(self, brawlerList):
        self._brawlerList = brawlerList

    def MapList(self):
        maplist= {
                "Penny": "Mina rocosa, Arcade de cristal, Espacio abierto",
                "Pam": "Brrumm Brrumm, Ultima parada",
                "Crow": "Claro del bosque, Avalancha Rocosa",
                "Leo": "Pradera traicionera, Escondite",
                "Ivy": "Canal grande, Crimen organizado",
                "Shelly": "loquesea",
                "Buzz": "prueba",
                "Meeple": "prueba 2 y 3"
               }
        brawl_map = maplist[self._brawlerList]
             
        return brawl_map

        


