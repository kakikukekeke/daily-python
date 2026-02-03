import pandas as pd
df = pd.read_csv("sample.csv")

print("aaa\n",df["japanease"])
print("iii\n",df[["japanease"]])
print("uuu\n",df[["japanease","math"]])
