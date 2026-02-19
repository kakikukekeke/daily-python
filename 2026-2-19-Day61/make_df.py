import pandas as pd
df = pd.read_csv("sample.csv")

dfB = pd.DataFrame()
dfB = df.iloc[1]

dfB
