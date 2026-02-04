import pandas as pd

df = pd.read_csv("sample.csv")
print(df)

df["art"] = [10,2,3]
print(df)

df.loc[3] = ["daniel",34,65,87,97,54,65]
print(df)
