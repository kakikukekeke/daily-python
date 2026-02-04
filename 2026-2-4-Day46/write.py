import pandas as pd

df = pd.read_csv("sample.csv")
kokugo = df.sort_values("japanease",ascending=False)

kokugo.to_csv("export.csv")
