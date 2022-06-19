import re
import requests
from bs4 import BeautifulSoup
import sys

def parsCL(productName):
    dataCL = []
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'old_design=0; _tuid=7950aa28d45fa8c00ceded31c1e7689b308b9864; _space=uln_cl%3A; ab_test=90x10v4%3A1%7Creindexer%3A2%7Cnew_designv10%3A1%7Cnew_designv13%3A1%7Cproduct_card_design%3A3%7Cdynamic_yield%3A3%7Cwelcome_mechanics%3A4%7Cdummy%3A20; ab_test_analytics=90x10v4%3A1%7Creindexer%3A2%7Cnew_designv10%3A1%7Cnew_designv13%3A1%7Cproduct_card_design%3A3%7Cdynamic_yield%3A3%7Cwelcome_mechanics%3A4%7Cdummy%3A20; _dy_csc_ses=t; _dy_c_exps=; _dycnst=dg; _dyid=-1342071815424360780; _dyfs=1653685939267; _dyjsession=d900b101eaa58df19942e7e6fea41f1a; _dy_cs_cookie_items=_dy_user_has_affinity; _gcl_au=1.1.499923116.1653685940; __ttl__widget__ui=1653685940850-7fb9ccc924f0; flixgvid=flixf067e646000000.79072290; __exponea_etc__=1204559e-7469-4a67-a1ee-bb01118ed09c; tmr_lvid=dc963ee64d9ffd3eba42d60330be9fa9; tmr_lvidTS=1653685942612; user_unic_ac_id=c4c0e7fa-f49b-4cd6-9d5a-0d542cb2e09a; advcake_trackid=70c06201-d403-c09c-9220-ceb91c63386c; _ym_uid=1653685943352967963; _ym_d=1653685943; _userGUID=0:l3oxwvyf:2V_0wR4y7PefQw6nG1hmyrEVq8e6nH8N; _dyid_server=-1342071815424360780; _dy_c_att_exps=; _hjSessionUser_1592904=eyJpZCI6Ijc5MzRhZTU3LTc3MjYtNTk1MC05NTcxLTg2ODBmNjE3OWZhNCIsImNyZWF0ZWQiOjE2NTM2ODU5NDAzODEsImV4aXN0aW5nIjp0cnVlfQ==; dy_fs_page=www.citilink.ru; advcake_track_id=6b2c8f7f-4a19-9f91-7040-d217cddb9816; advcake_session_id=62227e65-a7fe-9794-2b46-23e125a93abf; clientId=1400420469.1653685941; _tt_enable_cookie=1; _ttp=b2aca175-65a7-400b-85ee-4428ea770373; _dy_user_has_affinity=true; _dy_geo=RU.EU.RU_ULY.RU_ULY_Ulyanovsk; _dy_df_geo=Russia..Ulyanovsk; is_show_welcome_mechanics=1; _dycst=dk.w.c.ws.; _ym_isad=1; _gid=GA1.2.1124689926.1654685109; _dy_ses_load_seq=45261%3A1654713598695; mindboxDeviceUUID=f49b1d7c-8102-481e-bece-2886fed9c414; directCrm-session=%7B%22deviceGuid%22%3A%22f49b1d7c-8102-481e-bece-2886fed9c414%22%7D; _dy_lu_ses=d900b101eaa58df19942e7e6fea41f1a%3A1654713600657; _dy_toffset=-1; _dy_soct=1017831.1041429.1654709706*1017570.1030352.1654713598*1033770.1068198.1654713598*1036008.1075335.1654713598*1046273.1308988.1654713598*1008131.1012968.1654713598*1015299.1026209.1654713598*1015300.1026211.1654713600; _ga_DDRSRL2E1B=GS1.1.1654713601.10.0.1654713601.60; dSesn=5d0f1676-71f6-5edd-5aa0-8ecee45856d4; _dvs=0:l45xr667:pcObFpM2DWf0DHSo8aie1VjOuDtPWE6P; _hjSession_1592904=eyJpZCI6IjVmOGI1ZDJhLWUxMDMtNGY1My05MjgzLTZlZDgxNGQ0OWJjNyIsImNyZWF0ZWQiOjE2NTQ3MTM2MDEzMzksImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInSessionSample=0; _hjAbsoluteSessionInProgress=0; _ga=GA1.2.1400420469.1653685941; tmr_detect=1%7C1654713601695; __exponea_time2__=-0.3273453712463379; cto_bundle=upx6_l82elMzcTQ0eUZsbDNMb2FRZUpmMzY1czBkODg5WGlGYXlhSFZrZXQ1eXVDdmRsTWVqcTJqQ0xFNWRKU2RQdTZXMk9ZR1hEVTBBMzdGNnJDeVVTR0ZWaXM1MTRySFJJZWw2cmlQUThpRGtFcEpxUFp2d1FySWV0OE81S3VtTFFCUEQwZktQd0M3NFJZZmdUV2wlMkYxYXJhUSUzRCUzRA; AMP_TOKEN=%24NOT_FOUND; _dc_gtm_UA-5582449-6=1; _dc_gtm_UA-5582449-1=1; tmr_reqNum=313',
        'referer': 'https://www.citilink.ru/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
    }

    responce = requests.get(url = "https://www.citilink.ru/search/?text={}".format(productName), headers = headers)

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
        price += " руб."

        link = "https://www.citilink.ru/" + card.find("a", class_="ProductCardVertical__name").get('href')

        if not re.search("Чехол", name) and not re.search("Защит", name) and not re.search("Блок", name) and not re.search("Пленка", name) and not re.search("Адаптер", name) and not re.search("Накладка", name) and not re.search("Сете", name) and not re.search("Каб", name) and not re.search("Развет", name):
            dataCL.append(
                    [name, price,link]
                )

    end = ""
    el1 = ""
    el2 = ""
    for i in range(len(dataCL)):
        for j in range(len(dataCL)):
            el1 = dataCL[i][1]
            el2 = dataCL[j][1]
            el1 = el1[:-5]
            el2 = el2[:-5]
            el1 = re.sub(" ", "", el1)
            el2 = re.sub(" ", "", el2)
            el1 = int(el1)
            el2 = int(el2)
            if  el1 < el2 :
                dataCL[i],dataCL[j] = dataCL[j],dataCL[i]


    for line in dataCL:
        end = end + line[0]  + " " + line[1] + " " + line[2] + "\n"

    with open("endResoultCL.txt", "w") as file:
        #file.write("Argument List:" + str(sys.argv))
        file.write(end)
    print("yes")


#parsCL("iphone")

if __name__ == "__main__":
    allMes = ""
    nameDev = ""
    if len (sys.argv) > 1:
        for i in range(len(sys.argv) - 1):
            allMes = allMes + sys.argv[i+1] + " "

       #nameDev = re.sub(r"D:\OpenServer\domains\parserSite\parserSite\pars.py\\", "", allMes)
        nameDev = re.sub("pars.py", "", allMes)

        #print(nameDev)
        parsCL(nameDev)
    else:
        with open("endResoult.txt", "w") as file:
                #file.write("Argument List:" + str(sys.argv))
                file.write("Запрос пуст !")
        print("Запрос пуст")
