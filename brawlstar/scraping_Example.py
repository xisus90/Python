import re
import requests

 


        
data_url = "https://brawlify.com/es/brawlers/"
result = requests.get(data_url)
content = result.text
data_sequence = r'h6 mb-0">(.*?)</h2>'
datas = re.findall(data_sequence, str(content))

data_brawlers = []

for i in datas:
    data_brawlers.append(i)
    