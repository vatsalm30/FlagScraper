import requests
from bs4 import BeautifulSoup
import csv

def getdata(url):  
    r = requests.get(url)  
    return r.text  

htmldata = getdata("https://commons.wikimedia.org/wiki/City_flags")  
soup = BeautifulSoup(htmldata, 'html.parser')  
for item in soup.find_all('img', attrs={'class':'mw-file-element'}): 

    imgurl = item['src'].rsplit('/', 1)[0]

    thumbPos = imgurl.find('/thumb')
    if thumbPos != -1:
        imgurl = imgurl[:thumbPos] + imgurl[thumbPos+6:]
    if not imgurl.endswith(".svg"):
        continue
    cityName = item.get('alt')
    flagDict = {"cityName":cityName, "imgurl":imgurl}
    with open('flag.csv', 'a', newline='', encoding="utf-8") as csvfile:
        fieldnames = ['City Name', 'Image URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(flagDict)
