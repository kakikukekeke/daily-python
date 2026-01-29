import requests
from bs4 import BeautifulSoup

url_load = "https://www.ymori.com/books/python2nen/test2.html"
response = requests.get(url_load)
soup = BeautifulSoup(response.content,"html.parser")

for element in soup.find_all("a"):
    print(element.text)
    url = element.get("href")
    print(url)
