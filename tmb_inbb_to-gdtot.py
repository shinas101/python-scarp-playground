import requests
from bs4 import BeautifulSoup
import re
import json
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

link_inb = []
direct_gdtot = []

def getNewwp(Url):
    url = f"{Url}"
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')
    j = soup.find_all('input',{'name':'newwpsafelink'})
    f = str(j)
    k = re.findall(r'("[^\s]+")', f)
    newwp = k[2]
    return newwp

def getNewLink(newwp):
    data = {
    'humanverification': '1',
    'newwpsafelink': f"{newwp}"
    }

    response = requests.post('https://inbbotlist.com/',headers=headers, data=data)
    ss = BeautifulSoup(response.text,'lxml')
    j = ss.find_all('form',{'id':'wpsafelink-landing'})
    f = str(j)
    k = re.findall(r'(https[^\s]+/)', f)
    newLink = k[0]
    return newLink

def getGo(newwp,newLink):
    data = {
    'humanverification': '1',
    'newwpsafelink': f"{newwp}"
    }

    response1 = requests.post(f"{newLink}", headers=headers, data=data)
    soop = BeautifulSoup(response1.text,'lxml')
    j = soop.find_all('a',{'rel':'nofollow','style':'cursor:pointer'})
    f = str(j)
    k = re.findall(r'(https[^\s]+)', f)
    link = k[0]
    dd = requests.post(link,headers=headers)
    soupr = BeautifulSoup(dd.text,'lxml')
    jj = soupr.find_all('input')
    ff = str(jj)
    kk = re.findall(r'([a-zA-Z0-9]+=)', ff)
    x = link.replace('inbbotlist','drive.inbbotlist')
    if kk == []:
        direct_gdtot.append(x)
        print
        return "no"
    else:
        go = kk[3]
        return go

def driveNewwp(go):
    data = {
    'go': f"'{go}'",
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'null',
        'Alt-Used': 'drive.inbbotlist.com',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga_WGJ4NGL98N=GS1.1.1661183989.7.1.1661185999.0.0.0; _ga=GA1.1.1830011510.1661076501; __gads=ID=aa09164205ca8075-229c965cbcd500ab:T=1661076588:RT=1661076588:S=ALNI_MZms--Pgm0HksRmd-NMNUKNB6sBzA; __gpi=UID=000008d8e1fb4c39:T=1661076588:RT=1661173041:S=ALNI_MaocMBBpqyFEYep3HUawOYCigWzWQ; __cf_bm=X599jGwEvjcMdQV_3XZHWP_5gIFT_3Ye0CF5_SD6fQs-1661185828-0-Af97GEbN51Hpd1l5v2OxDHogKcraiBFaprXmJwJwJIdIgO+ByIPITqtNAJqT5daTcEDG3OUwzW7qxuOIgPO6RXu4PPf4Rx/PZpAWWYZoSwe9P4BclBhGv+5nJog/a3DAaQ==',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        }
    resonse = requests.post('https://drive.inbbotlist.com/',headers=headers, data=data)
    soupe = BeautifulSoup(response.text,'lxml')
    j = soupe.find_all('input',{'name':'newwpsafelink'})
    f = str(j)
    k = re.findall(r'("[^\s]+")', f)
    newwp1 = k[2]
    return newwp1

def drivegetNewLink(newwp1):
    data = {
    'humanverification': '1',
    'newwpsafelink': f"{newwp1}"
    }

    response = requests.post('https://drive.inbbotlist.com/',headers=headers, data=data)
    ss = BeautifulSoup(response.text,'lxml')
    j = ss.find_all('form',{'id':'wpsafelink-landing'})
    f = str(j)
    k = re.findall(r'(https[^\s]+/)', f)
    newLink1 = k[0]
    return newLink1
    
def driveLast(newwp1,newLink):
    data = {
    'newwpsafelink': f"{newwp1}"
    }

    response1 = requests.post(f"{newLink}", headers=headers, data=data)
    soop = BeautifulSoup(response1.text,'lxml')
    j = soop.find_all('a',{'rel':'nofollow','style':'cursor:pointer'})
    f = str(j)
    k = re.findall(r'(https[^\s]+=)', f)
    link1 = k[0]
    return link1

def lastres(link1):
    lastres = requests.get(f"{link1}", headers=headers)
    print(lastres.url)
    return lastres.url

def main(mainUrl):
    newwp = getNewwp(mainUrl)
    newlink = getNewLink(newwp)
    gof = getGo(newwp,newlink)
    if gof == "no":
        quit()
    else:
        newwp1 = driveNewwp(gof)
        drivenewlink = drivegetNewLink(newwp1)
        drivelast = driveLast(newwp1,drivenewlink)
        lastresp = lastres(drivelast)
        link_inb.append(lastresp)

with open(r'boss-inbbot.txt','r') as fl:
    for i in fl:
        main(i)


j=''
for i in inbbot:
	j+=f"{i}\n"

g = github.Github("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")
repo = g.get_repo("shinas101/miscellaneous")
contents = repo.get_contents("direct-gdtot.txt")
repo.update_file(contents.path, "rocketman", f"{j}", contents.sha, branch="main")


j=''
for i in tmb_redirect:
	j+=f"{i}\n"

g = github.Github("YOUR_GITHUB_TKN")
repo = g.get_repo("shinas101/miscellaneous")
contents = repo.get_contents("inbbot-link.txt")
repo.update_file(contents.path, "hesoyam", f"{j}", contents.sha, branch="main")
