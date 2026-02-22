import pandas as pd
df = pd.read_csv("sample.csv")

df.duplicated().value_counts()
