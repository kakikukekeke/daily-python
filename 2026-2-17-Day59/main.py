import json
from pprint import pprint
import requests
import tkinter as tk

def get_weather():
    Label_1.pack()
    Label_2.pack()
    Label_3.pack()
    Label_4.pack()
root = tk.Tk()
root.title("weather")
root.geometry("400x300")
key = "aea2c9e0afcf081dac7e698d18a5435c"
city = "286-0018,jp"
url = f"https://api.openweathermap.org/data/2.5/weather?zip={city}&appid={key}&units=metric&lang=ja"
jsondata = requests.get(url).json()

button = tk.Button(root,text="btn",command=get_weather)
button.pack()

jsondata = requests.get(url).json()
Label_1 = tk.Label(root,text=f"都市名 = {jsondata["name"]}")

Label_2 = tk.Label(root,text=f"気温 = {jsondata["main"]["temp"]}")

Label_3 = tk.Label(root,text=f"天気 = {jsondata["weather"][0]["main"]}")

Label_4 = tk.Label(root,text=f"天気詳細 = {jsondata["weather"][0]["description"]}")


tk.mainloop()
