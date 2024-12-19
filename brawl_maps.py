from dataclasses import dataclass
@dataclass 


class mapsforbrawler:
 
    def __init__(self, brawler):       
            self.brawlers = brawler


    def execute(self):
        brawler_maps = self.brawlersList()
        return brawler_maps    



#class BrawlSearch:

    
    def brawlersList(self, brawlid):
        brawlers = ["Penny", "Pam", "Crow", "Leo", "Ivy"]
        position = 0
        while position <= (len(brawlers)):
            if brawlers[position] == brawlid:
                goodmap = self.MapList(brawlers[position])
                return goodmap
            position += 1



#class MapSearch:

    def MapList(self, brawlers):
        
        pass


