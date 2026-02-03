import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

out_folder = Path("down2")
out_folder.mkdir(exist_ok=True)

for element in soup.find_all("img"):
    src = element.get("src")

    image_url = urllib.parse.urljoin(load_url,src)
    imgdata = requests.get(image_url)

    fileneme = image_url.split("/")[-1]
    out_path = out_folder.joinpath(fileneme)

    with open(out_path,mode="wb") as f:
        f.write(imgdata.content)

    time.sleep(1)
