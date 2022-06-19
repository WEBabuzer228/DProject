import re
import replace
import requests
from bs4 import BeautifulSoup
import sys

def parsKC(productName):
    dataKC = []
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'session_uuid=fb229cd1-d8ad-4b1f-8704-a00b97f49504; terminal=0; store[region]=deb1d05a-71ce-40d1-b726-6ba85d70d58f; store[kladr]=18000001000; store[city]=%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA; store[city_id]=1444; store[region_id]=150; _gcl_au=1.1.666419575.1654700421; rrpvid=68; tmr_lvid=4521c3b936849107f9daf538788074e3; tmr_lvidTS=1654700421916; _ym_uid=16547004221029843055; _ym_d=1654700422; _gid=GA1.2.1772114118.1654700422; _ym_isad=1; _userGUID=0:l45pwpfe:pEr669gY63DEOuWp60mPzxLraXIS4J~r; user_unic_ac_id=af1f4928-bbf3-a421-e1ed-2615f09baad3; advcake_trackid=cbf9433a-eba2-c09b-e929-2536133fdbfb; rcuid=61d15df9e4d2ec000125b6fc; cted=modId%3Droa8zt8u%3Bclient_id%3D1953711298.1654700422%3Bya_client_id%3D16547004221029843055; _ct_site_id=51314; _ct=2100000000012723003; g4c_x=1; _ct_client_global_id=539dd0fe-0151-50fa-933b-0d446b4e4cf7; _ga_VBSF5JSB9F=GS1.1.1654753509.3.0.1654753509.0; _ga=GA1.2.1953711298.1654700422; _gat=1; _ym_visorc=b; _ct_ids=roa8zt8u%3A51314%3A17902908; call_s=%3C!%3E%7B%22roa8zt8u%22%3A%5B1654755311%2C17902908%2C%7B%22241832%22%3A%22746724%22%7D%5D%2C%22d%22%3A2%7D%3C!%3E; _ct_session_id=17902908; tmr_detect=1%7C1654753510533; dSesn=8658260d-340d-dc99-a284-8e0511d327db; _dvs=0:l46likdq:_A8ZB2Dn8_aP1Ap7LMB491GDFAkr9Hpx; rrwpswu=true; _gat_UA-58067771-1=1; tmr_reqNum=96',
        'referer': 'https://kcentr.ru/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
    }

    responce = requests.get(url = "https://kcentr.ru/search/271/?q={}".format(productName), headers = headers)

    #responce = re.sub("\u20bd", " ", responce)

    with open(f"indexKC.html", "w", encoding='UTF8') as file:
        file.write(responce.text)
    with open("indexKC.html", encoding='UTF8') as file:
        src = file.read()

    src.replace("/*", " ")
    soup = BeautifulSoup(src, "lxml")
    cardName = soup.find_all("div", class_="prod")

    #print(cardName)

    for card in cardName:
        name = card.find("div", class_="prod__title-inner").text.strip()
        #price = card.find("div",class_="prod__price-current").text
        price = getattr(card.find("div",class_="prod__price-current"),'text',None)
        
        if price != None:
            price = price.replace('\n','')
            price = price.replace('\t', '')
            price = price[:-1] + 'руб.'
        else:
            continue

        link = "https://kcentr.ru" + card.find("a", class_="prod__title").get('href')

        if not re.search("Чехол", name) and not re.search("Защит", name) and not re.search("Блок", name) and not re.search("Пленка", name) and not re.search("Адаптер", name) and not re.search("Накладка", name) and not re.search("Сете", name) and not re.search("Каб", name) and not re.search("Развет", name):
            dataKC.append(
                    [name, price,link]
                )

        
        
    with open("endResoultKC.txt", "w", encoding='UTF8') as file:
        for data in dataKC:
            file.write(data[0] + " " + data[1] + " "+ data[2] + "\n")

if __name__ == "__main__":
    allMes = ""
    nameDev = ""
    if len (sys.argv) > 1:
        for i in range(len(sys.argv) - 1):
            allMes = allMes + sys.argv[i+1] + " "

       #nameDev = re.sub(r"D:\OpenServer\domains\parserSite\parserSite\pars.py\\", "", allMes)
        nameDev = re.sub("pars.py", "", allMes)

        #print(nameDev)
        parsKC(nameDev)
    else:
        with open("endResoultKC.txt", "w") as file:
                #file.write("Argument List:" + str(sys.argv))
                file.write("Запрос пуст !")
        print("Запрос пуст")
