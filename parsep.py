import requests
from bs4 import BeautifulSoup as bs
import lxml

dns_filters = {
    "1obzp7" : "AM5",
    "13iyb1" : "AM4",
    "19m8s3" : "LGA 1700",
    "13j0y6" : "LGA 1200",
    "13j0rf" : "LGA 1151-v2",
    "13j0al" : "LGA 1151",
    "13j087" : "LGA 1150",
    "13j0vf" : "LGA 1155",
    "13j0ya" : "LGA 2066",
    "13j0ye" : "sTRX4",
    "13j0yi" : "TR4",
    "19aqum" : "sWRX8",
    "13iyb0" : "AM3+",
    "13j07l" : "FM2+",
    "1qmvvz" : "FM2",
    "1jgqro" : "LGA 1156",
    "13j0yd" : "LGA 775",
    "13j0yc" : "LGA 478",
    "13iz8u" : "BGA1296", 
    "13iydn" : "BGA1170",
    "13iyb4" : "BGA1090",
    "13iyb3" : "BGA769",
    "1qmwme" : "FS1",
}

page = 1
socket = "lga1170"

url = f'https://zeon18.ru/computer-parts/power-supplies/'

r = requests.get(url)
soup = bs(r.content, 'lxml')
items = soup.find_all('a', class_="catalog-item-title")

print(items)
for item in items:
    print(item.text)