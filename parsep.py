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

# page = 1
# socket = "lga1170"

# url = f'https://www.newegg.com/p/pl?d=motherboard'

# r = requests.get(url)
# soup = bs(r.text, 'lxml')
# # items = soup.find_all('a', text = "Материнская плата MSI H510M-A PRO")

# print(soup)
# # for item in items:
# #     print(item.text)

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from typing import List, Tuple, Union


def parse(url: str) -> List[Tuple[str, str, str]]:
    options = Options()
    options.add_argument('--headless')

    items = []
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(0.5)
    
    while True:
        try:
            page = last_page = 1
            while page <= last_page:
                if page > 0:
                 url = f'https://www.citilink.ru/catalog/shiny/?p={page}'
            
            
            for item_el in driver.find_elements_by_css_selector("product_data__gtm-js product_data__pageevents-js  ProductCardVertical js--ProductCardInListing ProductCardVertical_normal ProductCardVertical_shadow-hover ProductCardVertical_separated"):
                

                try:
                    name = item_el.find_element_by_class_name('ProductCardVerticalLayout__wrapper-description ProductCardVertical__layout-description').text
                except NoSuchElementException:
                    name = ''

                try:
                    price = item_el.find_element_by_class_name('ProductPrice ProductPrice_default ProductCardVerticalPrice__price-current').text
                except NoSuchElementException:
                    price = '-'
                    
                row = name, price
                items.append(row)
            try:
               last_page = int(item_el.find_element_by_class_name('PaginationWidget__page js--PaginationWidget__page PaginationWidget__page_last PaginationWidget__page-link').text)
               page += 1   

            except NoSuchElementException:
                break
            
            
        finally:
            driver.quit()

    return items

if __name__ == '__main__':
    url = 'https://www.citilink.ru/catalog/shiny/?p=1'
    parse(url)