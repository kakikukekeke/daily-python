import pandas as pd

df = pd.read_csv("population.csv",index_col=
                 "全国・都道府県",encoding="UTF-8")

print(len(df))
print(df.columns.values)
