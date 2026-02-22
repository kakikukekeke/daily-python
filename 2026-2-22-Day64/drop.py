import pandas as pd
df = pd.read_csv("sample.csv")

dfB = df.drop_duplicates()
dfB
