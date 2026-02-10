import pandas as pd


df = pd.read_csv("12CHIBA.csv",header=None,encoding="shift_jis",dtype=str)
print(len(df))
print(df.columns.values)
