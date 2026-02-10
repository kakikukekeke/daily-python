import pandas as pd


df = pd.read_csv("12CHIBA.csv",header=None,encoding="shift_jis",dtype=str)

results = df[df[2] == "2860018"]
print(results[[2,6,7,8]])
