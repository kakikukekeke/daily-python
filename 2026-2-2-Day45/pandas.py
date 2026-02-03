import pandas as pd

df = pd.read_csv("sample.csv")

print("len",len(df))
print("colum",df.columns.values)
print("index",df.index.values)
print(df)
