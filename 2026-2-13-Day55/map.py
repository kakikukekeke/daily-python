import folium
import pandas as pd

df = pd.read_csv("watar.csv",encoding="shift-jis")
hygrand = df[["緯度","経度"]].values

m = folium.Map([35.956,136.184],zoom_start=16)
for data in hygrand:
    folium.Marker([data[0],data[1]]).add_to(m)
m.save("sabae.html")
