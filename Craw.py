import urllib.request
import requests
import re, os
from bs4 import BeautifulSoup
import socket

socket.setdefaulttimeout(15)
root_url = "https://irclogs.ubuntu.com/"
def isFile(url):
    return not url.endswith('/')
def docName(url):
    s = url.lstrip(root_url)
    return s
def getAll(URL):
    doc = docName(URL)
    if isFile(URL):
        if not os.path.exists(doc.replace("%23","#")):
            if doc.endswith("txt"):
                for i in range(5):
                    try:
                        print("Downloading "+doc.replace("%23","#")+"...")
                        urllib.request.urlretrieve(URL, doc.replace("%23","#"))
                        break
                    except:
                        print("ERROR:",i+1,"time(s)")
    else:
        if doc!="":
            os.makedirs(doc, exist_ok=True)
        urls = getUrls(URL)
        for u in urls:
            #print(u)
            getAll(u)

def getUrls(URL):
    for i in range(5):
        try:
            soup = BeautifulSoup(urllib.request.urlopen(URL).read(),"html.parser")
            texts = soup.find_all("a")[4:]
            #print(texts)
            urls = []
            for url in texts:
                u = str(url).split('"')[1]
                if u.startswith('/'):
                    continue
                urls.append(URL+u)
            #print(urls)
            return urls
        except:
            print("ERROR_URL:",i+1,"time(s)")
    return getUrls(URL)
    
#root = "Files/"
#print(getUrls("https://irclogs.ubuntu.com/2004/07/"))

getAll("https://irclogs.ubuntu.com/2021/")
