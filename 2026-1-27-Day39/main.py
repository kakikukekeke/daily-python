import requests
from bs4 import BeautifulSoup

url = "https://www.aozora.gr.jp/cards/000879/files/92_14545.html"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

print(soup)
