import requests
from bs4 import BeautifulSoup
import lxml
import re


myMovies = []
gdtotLinks = []
dateYear = ['https://gdrivemovies.xyz/2022/08/',
 'https://gdrivemovies.xyz/2022/07/',
 'https://gdrivemovies.xyz/2022/06/',
 'https://gdrivemovies.xyz/2022/05/',
 'https://gdrivemovies.xyz/2022/04/',
 'https://gdrivemovies.xyz/2022/03/',
 'https://gdrivemovies.xyz/2022/02/',
 'https://gdrivemovies.xyz/2022/01/',
 'https://gdrivemovies.xyz/2021/12/',
 'https://gdrivemovies.xyz/2021/10/',
 'https://gdrivemovies.xyz/2021/09/',
 'https://gdrivemovies.xyz/2021/08/',
 'https://gdrivemovies.xyz/2021/07/',
 'https://gdrivemovies.xyz/2021/06/',
 'https://gdrivemovies.xyz/2021/05/',
 'https://gdrivemovies.xyz/2021/01/',
 'https://gdrivemovies.xyz/2020/12/',
 'https://gdrivemovies.xyz/2020/10/',
 'https://gdrivemovies.xyz/2020/09/',
 'https://gdrivemovies.xyz/2020/08/']

headers = {
    'authority': 'gdrivemovies.xyz',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'referer': 'https://gdrivemovies.xyz/2022/08/page/2/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

def getLink(id=0,y=0):
    mainUrl = dateYear[y]+'page/'+str(id)
    html = requests.get(mainUrl,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    link = soup.find_all("a",{"class": "btn-readmore"})
    j = str(link)
    pat = re.compile('(?<=href=").*?(?=")')
    flink = pat.findall(j)
    print(mainUrl)
    print(flink)
    return flink

id = 0
y = 0
def getMovies(id,y):
    for i in range(10):
        id+=1
        myMovies.extend(getLink(id,y))
        print(id)
    
def dateFix(y):
    for i in range(20):
        getMovies(id,y)
        y+=1

print("	Started scraping ")       
dateFix(y)

print("	Gathering Links ")
for i in range(len(myMovies)):
    mainUrl = myMovies[i]
    html = requests.get(mainUrl, headers=headers,allow_redirects=False)
    soup = BeautifulSoup(html.text,'lxml')
    link = soup.find_all("a",{"class": "wp-block-button__link"})
    j = str(link)
    pat = re.compile('(?<=href=").*?(?=")')
    flink = pat.findall(j)
    gdtotLinks.extend(flink)
    print(mainUrl)
    print(flink)

with open(r'gdtot-links.txt', 'w') as fp:
    for link in gdtotLinks:
        fp.write("%s\n" % link)
    print('Done')
