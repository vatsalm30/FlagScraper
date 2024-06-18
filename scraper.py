import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, unquote


def getdata(url):  
    r = requests.get(url)  
    return r.text  

htmldata = getdata("https://vexillology.fandom.com/wiki/List_of_national_capital_flags")  
soup = BeautifulSoup(htmldata, 'html.parser')  
for item in soup.find_all('img', attrs={'class':'thumbimage'}): 
    imgurl = item['src']
    position = imgurl.find('/revision')
    if position != -1:
        imgurl = imgurl[:position]
    
    urllib.request.urlretrieve(imgurl, unquote(urlparse(imgurl).path.rsplit('/', 1)[-1]))
