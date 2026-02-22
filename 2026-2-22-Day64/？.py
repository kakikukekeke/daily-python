import pandas as pd
df = pd.read_csv("sample.csv")

dfB = df.copy()
num_cols = df.select_dtypes(include="number").columns
dfB[num_cols] = dfB[num_cols].fillna(df[num_cols].mean())
dfB
