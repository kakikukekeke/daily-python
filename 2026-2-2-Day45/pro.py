import requests 
from bs4 import BeautifulSoup
from pathlib import Path
import urllib.parse
import time

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url,timeout=10)
soup = BeautifulSoup(html.content,"html.parser")

out_folder = Path("down2")
out_folder.mkdir(exist_ok=True)

for element in soup.find_all("img"):
    src = element.get("src")
    if not src:
        continue

    image_url = urllib.parse.urljoin(load_url,src)
    imgdate = requests.get(image_url,timeout=10)

    if imgdate.status_code != 200:
        continue


    filename = image_url.split("/")[-1]
    out_path = out_folder / filename

    with open(out_path,"wb") as f:
        f.write(imgdate.content)

    time.sleep(1)
