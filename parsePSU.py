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

from selenium.webdriver import EdgeOptions

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
        with open("PSU_saves.json") as json:
            PSU_Dict = js.load(json)
    except:
        PSU_Dict = {
            'name':[],
            'formFactor':[],
            'power':[],
            'fan':[],
            'pin':[],
            'GPUpin':[],
            'price':[],
            'link' : []
        }

    page = 7
    start = len(PSU_Dict['name'])//48+1
    print(start)
    
    # options = EdgeOptions()
    # options.add_argument("--remote-allow-origins=http://localhost:55372")

    driver = webdriver.Edge()

    for i in range(start,8):    
        with open("PSU_saves.json", "w") as json:
            js.dump(PSU_Dict, json)

        page = i

        print("________________________")
        print("page: ", page)
        print("________________________")

        url = f'https://www.citilink.ru/catalog/bloki-pitaniya/?p={page}'

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
                name_ = name_[re.search("Блок питания", name_).end()+1:re.search(",", name_).start()]
                print(name_)
                PSU_Dict['name'].append(name_)
            except:
                try:
                    name = item.find("a", class_="app-catalog-1k0cnlg e1mnvjgw0")
                    name_ = str(name.text)
                    name_ = name_[re.search("Блок питания", name_).end()+1:re.search(",", name_).start()]
                    print(name_)
                    PSU_Dict['name'].append(name_)
                except Exception as e:
                    print(e)
                    PSU_Dict['name'].append('?')
                    

            try:
                link = "https://www.citilink.ru" + name.get("href")
                print(link)
            except:
                link = '?'
                print('?')

            try:
                form_factor = item.find(text=re.compile("Форм-фактор")).parent.next.next[:-1]
                print(form_factor)
                PSU_Dict["formFactor"].append(form_factor)
            except:
                print("?")
                PSU_Dict["formFactor"].append('?')

            try:
                power = item.find(text=re.compile("Мощность:")).parent.next.next[:-1]
                power_ = power[0:re.search(",", power).start()]
                print(power_)
                PSU_Dict["power"].append(power_)
            except:
                try:
                    power = item.find(text=re.compile("Мощность:")).next
                    power_ = power[0:re.search(",", str(power)).start()]
                    print(power_)
                    PSU_Dict["power"].append(power_)
                except Exception as e:
                    PSU_Dict["power"].append('?')
                    print(e)

                
            try:
                fan = item.find(text=re.compile("Вентилятор")).parent.next.next[:-1]
                fan = fan[0:re.search(",", fan).start()]
                print(fan)   
                PSU_Dict["fan"].append(fan)
            except:
                try:
                    fan = item.find(text=re.compile("Вентилятор:")).next
                    fan = fan[0:re.search(",", str(fan)).start()]
                    print(fan)
                    PSU_Dict["fan"].append(fan)
                except Exception as e:
                    PSU_Dict["fan"].append("?")
                    print(e)



            try:
                pin = item.find(text=re.compile("Разъемы")).parent.next.next[:-1]
                pin_ = pin[re.search("CPU", pin).end()+1:re.search(",", pin).start()]
                print(pin_)   
                PSU_Dict["pin"].append(pin_)
            except Exception as e:
                PSU_Dict["pin"].append("?")
                print(e)

            try:
                gpu_pin = pin[re.search("видеокарта", pin).end()+1:re.search("SATA", pin).start()-2]
                print(gpu_pin)   
                PSU_Dict["GPUpin"].append(gpu_pin)
            except Exception as e:
                PSU_Dict["GPUpin"].append("?")
                print(e)


            try:
                price = item.find('span', class_="e1j9birj0 e106ikdt0 app-catalog-j8h82j e1gjr6xo0").text
                price = price.replace(" ", "")
                price = int(price)
                print(price)
                PSU_Dict["price"].append(price)
            except Exception as e:
                PSU_Dict["price"].append("?")
                print(e)


            PSU_Dict['link'].append(link)

            # driver2.get(link+"properties/")

            # t.sleep(1.5)

            # html2 = driver2.page_source

            # soup2 = BeautifulSoup(html2)

            # try:
            #     maxRam = soup2.find(text=re.compile(" ГБ")).parent.text
            #     maxRam = maxRam[:-3]
            #     print(maxRam)
            #     PSU_Dict["maxRam"].append(maxRam)

            #     powerPin = soup2.find(text=re.compile(" pin ")).parent.text
            #     powerPin = powerPin[:-4]
            #     print(powerPin)
            #     PSU_Dict["powerPin"].append(powerPin)
            # except:
            #     maxRam = "?"
            #     print(soup2.find(text=re.compile("ГБ")))
            #     print(maxRam)
            #     PSU_Dict["maxRam"].append(maxRam)

            #     powerPin = "?"
            #     print(soup2.find(text=re.compile("pin")))
            #     print(powerPin)
            #     PSU_Dict["powerPin"].append(powerPin)


    df = pd.DataFrame(PSU_Dict)
    df.to_csv('data/PSU_DF.csv')
    print()
    print("-----------------------------------------------")
    print(df)
    print()
    print(PSU_Dict)
        
    

if __name__ == '__main__':
    parse()