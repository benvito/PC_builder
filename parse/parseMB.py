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
        with open("Motherboards_saves.json") as json:
            motherboardDict = js.load(json)
    except:
        motherboardDict = {
            'name':[],
            'formFactor':[],
            'socket':[],
            'chipset':[],
            'ramType':[],
            'ramSlots':[],
            'ramFreq':[],
            'maxRam':[],
            'powerPin':[],
            'price':[],
            'link' : []
        }

    page = 7
    

    driver = webdriver.Edge("C:\\msedgedriver\\msedgedriver.exe")
    driver2 = webdriver.Edge("C:\\msedgedriver\\msedgedriver.exe")

    for i in range(7,8):    
        with open("Motherboards_saves.json", "w") as json:
            js.dump(motherboardDict, json)

        page = i

        print("________________________")
        print("page: ", page)
        print("________________________")

        url = f'https://www.citilink.ru/catalog/materinskie-platy/?p={page}'

        driver.get(url)

        html = driver.page_source

        soup = BeautifulSoup(html)

        names = soup.find_all("div", class_="e12wdlvo0 app-catalog-1bogmvw e1loosed0")
        for item in names:
            print("________________________")
            print("item : ", names.index(item)+1, " / ", len(names))
            print("________________________")
            try:
                name = item.find("a", class_="app-catalog-9gnskf e1259i3g0")
                print(name.text)
                motherboardDict['name'].append(name.text)
            except:
                name = item.find("a", class_="app-catalog-1k0cnlg e1mnvjgw0")
                print(name.text)
                motherboardDict['name'].append(name.text)


            link = "https://www.citilink.ru" + name.get("href")
            print(link)

            try:
                formfactor = item.find(text=re.compile("Форм-фактор")).parent.next.next[:-1]
                print(formfactor)
                motherboardDict["formFactor"].append(formfactor)
                #mATX
            except:
                print("?")
                motherboardDict["formFactor"].append('?')

            try:
                socket = item.find(text=re.compile("Сокет")).parent.next.next[:-1]
                socket_ = socket[0:re.search(";", socket).start()]
                print(socket_)
                motherboardDict["socket"].append(socket_)
                #LGA 1200; чипсет: Intel H510
            except:
                motherboardDict["socket"].append("?")

            try:
                chipset = socket[re.search("; чипсет: ", socket).end():]
                print(chipset)
                motherboardDict["chipset"].append(chipset)
            except:
                motherboardDict["chipset"].append("?")

            try:
                ram = item.find(text=re.compile("Память")).parent.next.next[:-1]
                ramType = ram[:re.search("- ", ram).start()]
                print(ramType)   
                motherboardDict["ramType"].append(ramType)
            except:
                motherboardDict["ramType"].append("?")

            try:
                ramSlots = int(ram[re.search("- ", ram).end():re.search("слота", ram).start()])
                print(ramSlots)
                motherboardDict["ramSlots"].append(ramSlots)
            except:
                motherboardDict["ramSlots"].append("?")

            try:
                ramFreq = int(ram[re.search("до ", ram).end():re.search("МГц", ram).start()])
                print(ramFreq)
                motherboardDict["ramFreq"].append(ramFreq)
            except:
                motherboardDict["ramFreq"].append("?")

            try:
                price = item.find('span', class_="e1j9birj0 e106ikdt0 app-catalog-j8h82j e1gjr6xo0").text
                price = price.replace(" ", "")
                price = int(price)
                print(price)
                motherboardDict["price"].append(price)
            except:
                motherboardDict["price"].append("?")


            motherboardDict['link'].append(link)

            driver2.get(link+"properties/")

            t.sleep(1.5)

            html2 = driver2.page_source

            soup2 = BeautifulSoup(html2)

            try:
                maxRam = soup2.find(text=re.compile(" ГБ")).parent.text
                maxRam = maxRam[:-3]
                print(maxRam)
                motherboardDict["maxRam"].append(maxRam)

                powerPin = soup2.find(text=re.compile(" pin ")).parent.text
                powerPin = powerPin[:-4]
                print(powerPin)
                motherboardDict["powerPin"].append(powerPin)
            except:
                maxRam = "?"
                print(soup2.find(text=re.compile("ГБ")))
                print(maxRam)
                motherboardDict["maxRam"].append(maxRam)

                powerPin = "?"
                print(soup2.find(text=re.compile("pin")))
                print(powerPin)
                motherboardDict["powerPin"].append(powerPin)


    df = pd.DataFrame(motherboardDict)
    df.to_csv('data/MB_DF.csv')
    print()
    print("-----------------------------------------------")
    print(df)
    print()
    print(motherboardDict)
        
    

if __name__ == '__main__':
    with open("Motherboards_saves.json") as json:
        motherboardDict = js.load(json)
    df = pd.DataFrame(motherboardDict)
    df.to_csv('data/MB_DF.csv')