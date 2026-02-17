import json
from pprint import pprint
import requests
from datetime import datetime,timedelta,timezone
import pandas as pd 
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Hiragino Maru Gothic Pro",
                                   "Hiragino sans","BIZ UDGothic","MS Gothic"]


key = "aea2c9e0afcf081dac7e698d18a5435c"
city = "286-0018,jp"
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&units=metric&lang=ja"
jsondata = requests.get(url).json()
df = pd.DataFrame(columns=["気温"])
tz = timezone(timedelta(hours=+9),"JST")
for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"],tz))[:-9]
    weather = dat["weather"][0]["description"]
    temp = dat["main"]["temp"]
    print("日時:{jst},天気:{w},気温:{t}度".format(jst=jst,w=weather,t=temp))
    df.loc[jst] = temp

df.plot(figsize=(15,8))
plt.ylim(-10,40)
plt.grid()
plt.show()
