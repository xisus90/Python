import re
from dataclasses import dataclass
import requests
@dataclass
 


class mapsforbrawler:
 
    def __init__(self, brawler):       
            self._brawler = brawler


    def execute(self):
        brawler_exists = BrawlersDataMemory().exists(self._brawler)
        if not brawler_exists:
            return "No existe brawler"

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
        self._brawlerList = ["Penny", "Pam", "Crow", "Leo", "Ivy"]

    def get_brawlers(self):
        return self._brawlerList

    def exists(self, brawler):
        return brawler in self._brawlerList


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

        


