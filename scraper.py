import requests  
from bs4 import BeautifulSoup  
    
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
    item["src"] = imgurl
    print(item["src"])