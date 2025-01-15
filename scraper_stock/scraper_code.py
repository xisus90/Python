import re
import requests
from bs4 import BeautifulSoup



#class LookingDataPlatform:
    
 #   def looking_platforms(self, platform):
 #       data_platforms = {
 #                       "Battle.net": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=battle.net&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
  #                      "Epic Games": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=epic+games&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
   #                     "GoG.com": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=gog.com&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
    #                    "Microsoft Store": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=microsoft+store&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
     #                   "Nintendo Eshop": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=nintendo+eshop&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
     #                   "Ea App": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=ea+app&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
     #                   "PlayStation Store": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=playstation+store&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
     #                   "RockStar": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=rockstar&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
     #                   "Steam":"https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=steam&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
     #                   "Ubisoft":"https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=ubisoft+connect&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query="
     #                   }
     #   platform_link = data_platforms[platform]
        
     #   return platform_link


class SearchGame:

    def __init__(self, game):       
            self._game = game
            #self._platform = platform

    def search(self):
        #search_platform = LookingDataPlatform().looking_platforms(self._platform)
        price_game = self.Lookingdataprice()
        return price_game
        
    def Lookingdataprice(self):
 
        data_url = "https://www.dlcompare.es/juegos"
        result = requests.get(data_url)
        print(result)
        if result.status_code == 200:
            filter = BeautifulSoup(result.text, "html.parser")
            games = filter.find_all('a', {'class': re.compile('game-list-item')}, title = True)
            
            for game in games:
                title_text = game['title']
                name_game = title_text.split('"')[0]
                print(name_game)

            game_titles = filter.find_all('span', {'class':'name'})
            for game_title in game_titles:
                game_text = game_title.text.split()
                print(game_text)


            #return games
             