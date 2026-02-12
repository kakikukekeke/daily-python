import pandas as pd

df = pd.read_csv("temp.csv",index_col="時点",skiprows=1)
df2 = pd.read_csv("top_temp.csv",index_col="時点",skiprows=1)
df3 = pd.read_csv("low_temp.csv",index_col="時点",skiprows=1)


print(df.columns.values)
print(df2.columns.values)
print(df3.columns.values)
