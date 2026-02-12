import pandas as pd 
df = pd.read_csv("watar.csv",encoding="shift-jis")

print(len(df))
print(df.columns.values)
