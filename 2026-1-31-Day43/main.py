import requests
from bs4 import BeautifulSoup
import urllib

url_load = "https://www.ymori.com/books/python2nen/test2.html"
response = requests.get(url_load)
soup = BeautifulSoup(response.content,"html.parser")
filename = "linklist.txt"
with open(filename,"w") as f:


    for element in soup.find_all("a"):
        print(element.text)
        url = element.get("href")
        link_url = urllib.parse.urljoin(url_load,url)
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")
