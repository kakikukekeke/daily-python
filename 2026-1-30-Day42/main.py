import requests
from bs4 import BeautifulSoup
import urllib

url_load = "https://www.ymori.com/books/python2nen/test2.html"
response = requests.get(url_load)
soup = BeautifulSoup(response.content,"html.parser")

for element in soup.find_all("a"):
    print(element.text)
    url = element.get("href")
    link_url = urllib.parse.urljoin(url_load,url)
    print(link_url)
    print(url)
