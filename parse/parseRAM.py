import requests
from bs4 import BeautifulSoup as bs
import lxml

import regex as re

import time as t

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time

# from selenium.webdriver import EdgeOptions

from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import json as js

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

def parse():
    try:
        with open("RAM_saves.json") as json:
            RAM_Dict = js.load(json)
    except:
        RAM_Dict = {
            'name':[],
            'count':[],
            'capacity':[],
            'freq':[],
            'timings':[],
            'formFactor':[],
            'type':[],
            'price':[],
            'link' : []
        }

    page = 7
    start = len(RAM_Dict['name'])//48+1
    print(start)
    
    # options = EdgeOptions()
    # options.add_argument("--remote-allow-origins=http://localhost:55372")
    # driver_path = 'C:\msedgedriver\msedgedriver.exe'

    # # Создаем объект Service, передавая путь к исполняемому файлу
    # service = Service(driver_path)

    # # Создаем объект EdgeOptions и настраиваем его по вашим потребностям
    # options = EdgeOptions()
    # # ...

    # # Создаем экземпляр драйвера, передавая объект Service и объект EdgeOptions
    # driver = Edge(service=service, options=options)

    driver = webdriver.Edge()


    for i in range(start,14):    
        with open("RAM_saves.json", "w") as json:
            js.dump(RAM_Dict, json)

        page = i

        print("________________________")
        print("page: ", page)
        print("________________________")

        url = f'https://www.citilink.ru/catalog/moduli-pamyati/?p={page}&view_type=list'

        driver.get(url)

        t.sleep(1)

        html = driver.page_source

        soup = BeautifulSoup(html)

        names = soup.find_all("div", class_="e12wdlvo0 app-catalog-1bogmvw e1loosed0")
        for item in names:
            print("________________________")
            print("item : ", names.index(item)+1, " / ", len(names))
            print("________________________")
            try:
                name = item.find("a", class_="app-catalog-9gnskf e1259i3g0")
                name_ = str(name.text)
                name__ = str(name.text)
                name_ = name_[re.search("Оперативная память", name_).end()+1:re.search("DDR", name_).start()]
                print(name_)
                RAM_Dict['name'].append(name_)
            except:
                try:
                    name = item.find("a", class_="app-catalog-1k0cnlg e1mnvjgw0")
                    name_ = str(name.text)
                    name__ = str(name.text)
                    name_ = name_[re.search("Оперативная память", name_).end()+1:re.search("DDR", name_).start()]
                    print(name_)
                    RAM_Dict['name'].append(name_)
                except Exception as e:
                    print(e)
                    RAM_Dict['name'].append('?')
                    

            try: 
                type_ = name__[re.search("DDR", name__).start():re.search(r"DDR\d", name__).end()+1]
                print(type_)
                RAM_Dict['type'].append(type_)
            except Exception as e:
                print(e)


            try:
                link = "https://www.citilink.ru" + name.get("href")
                print(link)
            except:
                link = '?'
                print('?')


            try:
                count = item.find(text=re.compile("Объем")).parent.next.next[:-1]
                count_ = count[0:re.search("х", count).start()]
                print(count_)
                RAM_Dict["count"].append(count_)
            except:
                print("?")
                RAM_Dict["count"].append('?')


            try:
                capacity = item.find(text=re.compile("Объем")).parent.next.next[:-1]
                capacity_ = capacity[re.search("х", capacity).start()+2:re.search("ГБ", capacity).start()-1]
                print(capacity_)
                RAM_Dict["capacity"].append(capacity_)
            except Exception as e:
                print(e)
                RAM_Dict["capacity"].append('?')


            try:
                freq = item.find(text=re.compile("Частота:")).parent.next.next[:-1]
                freq_ = freq[0:re.search("МГц", freq).start()]
                print(freq_)
                RAM_Dict["freq"].append(freq_)
            except:
                try:
                    freq = item.find(text=re.compile("Частота:")).next
                    freq_ = freq[0:re.search("МГц", str(freq)).start()]
                    print(freq_)
                    RAM_Dict["freq"].append(freq_)
                except Exception as e:
                    RAM_Dict["freq"].append('?')
                    print(e)

                
            try:
                timings = item.find(text=re.compile("Тайминги")).parent.next.next[:-1]
                timings_ = timings[0:re.search(";", timings).start()]
                print(timings_)   
                RAM_Dict["timings"].append(timings_)
            except:
                try:
                    timings = item.find(text=re.compile("Тайминги:")).next
                    timings_ = timings[0:re.search(";", str(timings)).start()]
                    print(timings_)
                    RAM_Dict["timings"].append(timings_)
                except Exception as e:
                    RAM_Dict["timings"].append("?")
                    print(e)



            try:
                formFactor = item.find(text=re.compile("Форм-фактор")).parent.next.next[:-1]
                formFactor_ = formFactor[0:re.search(";", formFactor).start()]
                print(formFactor_)   
                RAM_Dict["formFactor"].append(formFactor_)
            except:
                try:
                    formFactor = item.find(text=re.compile("Форм-фактор:")).next
                    formFactor_ = formFactor[0:re.search(";", str(formFactor)).start()]
                    print(formFactor_)
                    RAM_Dict["formFactor"].append(formFactor_)
                except Exception as e:
                    RAM_Dict["formFactor"].append("?")
                    print(e)


            try:
                price = item.find('span', class_="e1j9birj0 e106ikdt0 app-catalog-j8h82j e1gjr6xo0").text
                price = price.replace(" ", "")
                price = int(price)
                print(price)
                RAM_Dict["price"].append(price)
            except Exception as e:
                RAM_Dict["price"].append("?")
                print(e)


            RAM_Dict['link'].append(link)


    df = pd.DataFrame(RAM_Dict)
    df.to_csv('sourceData/RAMdry.csv')
    print()
    print("-----------------------------------------------")
    print(df)
    print()
    print(RAM_Dict)
        
    

if __name__ == '__main__':
    parse()