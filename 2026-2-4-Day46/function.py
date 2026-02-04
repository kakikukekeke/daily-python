import pandas as pd

df = pd.read_csv("sample.csv")

print(df["math"].max())
print(df["math"].min())
print(df["math"].mean())
print(df["math"].median())
print(df["math"].sum())
