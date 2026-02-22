import pandas as pd
df = pd.read_csv("sample.csv")

dfB = df.dropna(subset=["social"])
dfB
