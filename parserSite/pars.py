# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import sys

def parsEldorado(productName):
    dataEldorado = []

    headers = {
        'Cookie': '__zzatgib-w-eldorado=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VgcmogZkxhIgseF39fIlI0cGMMRA9fP0kncxs3V10cESRYDiE/C2lbVjRnFRtASBgvS255Lj5uIWROXCRDXFV1F2BKQys2FkZGHHIzdz9rCCIZURMqX3hHV2tlVUI4MWcMT09NEhY=oBZa2Q==; cfidsgib-w-eldorado=iPsDpJH4bglX53cMNq+HEJWEi1MoG2GGHlwzgjBy+i7n6efy/GgRZJq01R8jb6UQqVzOfYulBdfEQpFGS+3zHshg+Omx+Y8qcCiHE6oFZ/NJXY3eBIounOYbSIkcPmlI4KOB+RVUSWRrYOlV6WaHbjLiu77GWGs+aMu4Pg==; tmr_reqNum=106; gsscgib-w-eldorado=QgeJ9rNPI7x1glkS4PeN/CC+zoZ9oDconmw6yzsSS6PWhsFfkFUQjmow1xXIC0mcAVHn6LVGq6fRjVY9w2gBb/df7UkCCMDoxPb7PL730xF21Q7pk6G/Nh2D8q7CPltgVVKeBuWZeAio9EJ3ckGL0wo94it+qeaUMiWsieRdJ4bhFvE15E6k9EsZLkTGV9W/3TrCqEXKWVvD/r20fseZBYVA3k73sQUWWidIpg+n2R+HT6bDYw9M+4mTLslNBw==; _dvs=0:l3t8kyse:k1ZB65GSArH~Q~v0fppHXpGek66xlNXo; _userGUID=0:l3ss5vqt:3nnvs5LtIlX9GW9X3P7AizbfgCP0y88P; _dy_c_exps=; _dy_df_geo=Russia..; _dy_geo=RU.EU.RU_.RU__; _dy_soct=1009413.1015420.1653918150.wk4p2k28anydu3c6xsdnnh4h8hz9lqn9*1009413.1015421.1653945725.wk4p2k28anydu3c6xsdnnh4h8hz9lqn9*1020255.1036209.1653945728.wk4p2k28anydu3c6xsdnnh4h8hz9lqn9*1029321.1119670.1653945734*1062106.1161327.1653945734*1066273.1175622.1653945734*1070841.1192040.1653945734*1091607.1268272.1653945734*1101806.1303953.1653945734*1003181.1004426.1653945734*1096798.1286433.1653945734*1047863.1186619.1653945734*1048763.1117338.1653945734*1048769.1117349.1653945734*1028959.1056007.1653945734*1024438.1090852.1653945735*1041165.1093592.1653945735; _dy_toffset=-1; _dycnst=dg; _dycst=dk.m.s.ws.; _dyid=-8800032794054702652; _ga=GA1.2.348736830.1653918149; _ga_4P3TZK55KZ=GS1.1.1653945726.2.1.1653945735.0; _gid=GA1.2.1447309133.1653918149; clickcake_clicks_history=%7B%2220220530%22%3A10%2C%2220220531%22%3A2%7D; clickcake_current=12; clickcake_max=12; clickcake_sessions_depth=%7B%2287797664-05e9-7121-ad51-5e799acfcefe%22%3A2%7D; clickcake_sessions_history=%7B%2220220530%22%3A8%2C%2220220531%22%3A2%7D; clickcake_total=12; tmr_lvid=1278774a8ac2f6acbffe0c556d7aeff7; tmr_lvidTS=1653918148919; show_region_popup=0; tmr_detect=1%7C1653945735165; _dy_c_att_exps=; _dy_csc_ses=wk4p2k28anydu3c6xsdnnh4h8hz9lqn9; _dyjsession=wk4p2k28anydu3c6xsdnnh4h8hz9lqn9; rcuid=6294c9c4ae90740001b4c684; rr-testCookie=testvalue; rrpvid=126; AUTORIZZ=0; bonus_cobrand_showed=0; ek_ab_test=B; el_group_user_org=0; lv_user_org=0; iRegionSectionId=11324; clickcake_rsid=87797664-05e9-7121-ad51-5e799acfcefe; clickcake_sid=513c1d21-cc33-9318-eeae-c1836fdef923; dSesn=f4b9491c-5726-4061-ec0f-4541c1d82bc1; _dc_gtm_UA-44012634-4=1; BITRIX_SM_SALE_UID=30923771917; _dyfs=1653921983368; uxs_uid=5ba16fb0-e01e-11ec-91ef-57c011f72065; _ym_d=1653918149; _ym_isad=1; _ym_uid=16539181493303889; advcake_click_id=; advcake_session_id=8b4a767d-6e24-a6ea-0aa0-167d6a24c6fe; advcake_track_url=https%3A%2F%2Fwww.eldorado.ru%2F; advcake_trackid=1395af48-5e0f-ff8f-82aa-ca5350bf7ba0; advcake_utm_partner=; advcake_utm_webmaster=; clickcake_id=50a2dd1d-7485-8cb5-325f-bec9b8a7b901; flocktory-uuid=234f9b3b-e50d-45f1-885a-f9b4fe19ccd1-5; st_uid=ad5d14cce7876256835cbaa91ce1da98; _gcl_au=1.1.491401147.1653918148; dy_fs_page=www.eldorado.ru; last_source=www.google.com; ABT_test=D; AC=1; _dyid_server=-8800032794054702652; _dyjsession=wk4p2k28anydu3c6xsdnnh4h8hz9lqn9; dt=1; PHPSESSID=gg537583pqr6j9qe5pem4428b0; __lhash_=3e03569fcced589f0b4f3ce81ed0af04; ab_segment=27; ab_user=2703922220100',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'www.eldorado.ru',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15',
        'Accept-Language': 'ru',
        'Referer': 'https://www.eldorado.ru/',
        'Connection': 'keep-alive'

        }


    response = requests.get(url="https://www.eldorado.ru/search/catalog.php?q={}".format(productName), headers = headers)
    #print("https://www.eldorado.ru/search/catalog.php?q={}".format(productName))



    with open(f'indexED.html', 'w') as file:
        file.write(response.text)
    
    with open('indexED.html') as file:
        src = file.read()
    
    soup = BeautifulSoup(src, 'lxml')

    findNameDevice = soup.find_all('li', class_="_F")
    dataEldorado = []
    EndRes = ""

    for nameDev in findNameDevice:

        name = nameDev.find("a", class_= "iG").text.strip()
        price = nameDev.find("span", class_= "OS VS").text.strip()
        link = "https://www.eldorado.ru/" + nameDev.find('a', class_='iG').get('href')

        price = re.sub("\xa0", " ", price)
        name = re.sub("\xa0", " ", name)


        if not re.search("Чехол", name) and not re.search("Защит", name) and not re.search("Блок", name) and not re.search("Адаптер", name) and not re.search("Накладка", name) and not re.search("Сете", name) and not re.search("Каб", name) and not re.search("Развет", name) and not re.search("Беспроводные", name):
            dataEldorado.append(
                    [name, price, link]
                )

    end = ""
    el1 = ""
    el2 = ""
    for i in range(len(dataEldorado)):
        for j in range(len(dataEldorado)):
            el1 = dataEldorado[i][1]
            el2 = dataEldorado[j][1]
            el1 = el1[:-5]
            el2 = el2[:-5]
            el1 = re.sub(" ", "", el1)
            el2 = re.sub(" ", "", el2)
            el1 = int(el1)
            el2 = int(el2)
            if  el1 < el2 :
                dataEldorado[i],dataEldorado[j] = dataEldorado[j],dataEldorado[i]

    for line in dataEldorado:
        end = end + line[0]  + " " + line[1] + " " + line[2] + "\n"

    with open("endResoult.txt", "w") as file:
        #file.write("Argument List:" + str(sys.argv))
        file.write(end)
    print("yes")




if __name__ == "__main__":
    allMes = ""
    nameDev = ""
    if len (sys.argv) > 1:
        for i in range(len(sys.argv) - 1):
            allMes = allMes + sys.argv[i+1] + " "

       #nameDev = re.sub(r"D:\OpenServer\domains\parserSite\parserSite\pars.py\\", "", allMes)
        nameDev = re.sub("pars.py", "", allMes)

        #print(nameDev)
        parsEldorado(nameDev)
    else:
        with open("endResoult.txt", "w") as file:
                #file.write("Argument List:" + str(sys.argv))
                file.write("Запрос пуст !")
        print("Запрос пуст")