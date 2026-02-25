import pandas as pd
df = pd.read_csv("sample.csv")

print(df.iloc[0]["japanease"])
print(df["japanease"].mean(numeric_only=True))
