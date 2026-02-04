import pandas as pd

df = pd.read_csv("sample.csv")

kokugo = df.sort_values("japanease",ascending=False)
suugaku = df.sort_values("math")
print(kokugo)
print(suugaku)
