import pandas as pd
df = pd.read_csv("sample.csv")

dfB = pd.DataFrame()
dfB = df[(df["japanease"] > 20) & (df["math"] > 20)]
dfB
