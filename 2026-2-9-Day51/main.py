import pandas as pd


df = pd.read_csv("12CHIBA.csv",header=None,encoding="shift_jis",dtype=str)

results = df[df[8] == "吾妻"]
print(results[[2,6,7,8]])

results = df[df[8].str.contains("吾妻")]
print(results[[2,6,7,8]])
