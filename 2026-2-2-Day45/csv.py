import pandas as pd
import random

names = ["ken","taito","leona","rihito","ukyo","komatu",]

data = {
    "name":names,
    "japanease":[random.randint(1,100) for _ in names],
    "math":[random.randint(1,100) for _ in names],
    "english":[random.randint(1,100) for _ in names],
    "sience":[random.randint(1,100) for _ in names],
    "social":[random.randint(1,100) for _ in names],
}

df = pd.DataFrame(data)

df.to_csv("sample.csv",index=False,encoding="utf-8-sig")
