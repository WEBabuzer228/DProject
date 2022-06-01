import re
import requests
from bs4 import BeautifulSoup

def parsCL(productName):
    dataCL = []
    headers = {
        'Accept':'',
        'User-Agent':'',
    }

    responce = requests.get(url = "https://www.citilink.ru/search/?text={}".format(productName))

    #responce = re.sub("/*", " ", responce)

    with open("indexCL.html", "w") as file:
        file.write(responce.text)
    with open("indexCL.html") as file:
        src = file.read()

    src.replace("/*", " ")
    soup = BeautifulSoup(src, "lxml")
    cardName = soup.find_all("div", class_="product_data__gtm-js product_data__pageevents-js ProductCardVertical js--ProductCardInListing ProductCardVertical_normal ProductCardVertical_shadow-hover ProductCardVertical_separated")

    #print(cardName)

    for card in cardName:
        name = card.find("a", class_="ProductCardVertical__name").text.strip()
        price = card.find("span",class_="ProductCardVerticalPrice__price-current_current-price").text.strip()

        if not re.search("Чехол", name) and not re.search("Защит", name) and not re.search("Блок", name) and not re.search("Адаптер", name) and not re.search("Накладка", name) and not re.search("Сете", name) and not re.search("Каб", name) and not re.search("Развет", name):
            dataCL.append(
                    [name, price]
                )

    for i in range(len(dataCL)):
        print(dataCL[i])


parsCL("iphone")