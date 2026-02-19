import pandas as pd
df = pd.read_csv("sample.csv")

dfB = pd.DataFrame()
df = df.drop("japanease",axis=1)
df
