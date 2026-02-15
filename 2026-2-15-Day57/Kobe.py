import json
from pprint import pprint
import requests

key = "aea2c9e0afcf081dac7e698d18a5435c"
city = "Kobe,JP"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},jp&appid={key}&units=metric&lang=ja"


jsondata = requests.get(url).json()
pprint(jsondata)
