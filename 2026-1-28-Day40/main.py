import requests
from bs4 import BeautifulSoup

url = "https://www.aozora.gr.jp/cards/000879/files/92_14545.html"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

title = soup.find("h1",class_="title")
print(title.text)
author = soup.find("h2",class_="author")
print(author.text)
content = soup.find("div",class_="main_text")
print(content.text)
