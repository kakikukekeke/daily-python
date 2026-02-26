import pandas as pd
df = pd.read_csv("sample.csv")

print(df.iloc[0]["japanease"])
print(df.mode(numeric_only=True))
