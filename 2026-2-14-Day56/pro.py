import folium
import pandas as pd
from datetime import datetime

df = pd.read_csv("store.csv")

m = folium.Map([35.946695,136.181993], zoom_start=16)
now = datetime.now().time()

for _, row in df.iterrows():
    try:
        lat = float(row["緯度"])
        lon = float(row["経度"])
    except:
        continue

    name  = row["店舗名(日本語)"]
    phone = row["電話番号"]
    start = row["営業開始時間"]
    end   = row["営業終了時間"]

    # 営業時間が無い店
    if pd.isna(start) or pd.isna(end):
        color = "blue"
        status = "営業時間不明"
        time_text = "不明"

    else:
        start = str(start)
        end   = str(end)

        try:
            start_time = pd.to_datetime(start).time()
            end_time   = pd.to_datetime(end).time()
        except:
            continue

        if start_time <= end_time:
            is_open = start_time <= now <= end_time
        else:
            is_open = now >= start_time or now <= end_time

        color  = "green" if is_open else "red"
        status = "営業中" if is_open else "閉店"
        time_text = f"{start} - {end}"

    popup = f"""
    <b>{name}</b><br>
    📞 {phone}<br>
    🕒 {time_text}<br>
    <b>{status}</b>
    """

    folium.Marker(
        [lat, lon],
        tooltip=name,
        popup=popup,
        icon=folium.Icon(color=color)
    ).add_to(m)

m.save("store.html")
