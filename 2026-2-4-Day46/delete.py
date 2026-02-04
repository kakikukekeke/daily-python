import pandas as pd

df = pd.read_csv("sample.csv")

print(df.drop("name",axis=1))
print(df.drop(2,axis=0))
