import re
import requests



class SearchGame:

    def __init__(self, game, platform):       
            self._game = game
            self._platform = platform

    def search(self):

        search_platform = LookingDataPlatform().looking_platforms(self._platform)
        #price_game = SearchPrice(self._search_platform)
        return search_platform
        
class LookingDataPlatform:
        
    def __init__(self, platform):
        self._platform = platform
        
    def looking_platforms(self):
        data_platforms = {
                        "Battle.net": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=battle.net&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
                        "Epic Games": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=epic+games&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
                        "GoG.com": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=gog.com&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
                        "Microsoft Store": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=microsoft+store&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
                        "Nintendo Eshop": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=nintendo+eshop&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
                        "Ea App": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=ea+app&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
                        "PlayStation Store": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=playstation+store&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
                        "RockStar": "https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=rockstar&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
                        "Steam":"https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=steam&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=",
                        "Ubisoft":"https://www.instant-gaming.com/es/busquedas/?platform%5B%5D=&type%5B%5D=ubisoft+connect&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query="
                        }
        platform_link = data_platforms[self._platform]
        
        return platform_link


#class SearchPrice():
        
#        def __init__(self):
#            data_url = ""
#            result = requests.get(data_url)
#            content = result.text
#            print (content)
            #data_sequence = r'h6 mb-0">(.*?)</h2>'
            #datas = re.findall(data_sequence, str(content))

            #self._data_brawlers = []

            #for i in datas:
            #    self._data_brawlers.append(i

            #pass  