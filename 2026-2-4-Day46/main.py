import pandas as pd 

df = pd.read_csv("sample.csv")

print(df.loc[2])
print(df.loc[[2]])
print(df.loc[[1,2]])
print(df.loc[2]["japanease"])
