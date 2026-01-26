import requests
from bs4 import BeautifulSoup

url = "https://www.ymori.com/books/python2nen/test2.html"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

chpt2 = soup.find(id="chap2")
for element in chpt2.find_all("li"):
    print(element.text)
