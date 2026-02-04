import pandas as pd

df = pd.read_csv("sample.csv")

data_s = df[df["japanease"] >= 20]
print(data_s)

data_c = df[df["math"] < 40]
print(data_c)
