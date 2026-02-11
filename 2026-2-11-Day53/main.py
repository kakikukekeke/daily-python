import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Hiragino Maru Gothic Pro",
"Hiragino sans" , "BIZ UDGothic","MS Gothic"]

df = pd.read_csv("population.csv",index_col=
                 "全国・都道府県",encoding="UTF-8")
print(df["2022年"])
df["2022年"].plot.bar()
plt.show()

print(len(df))
print(df.columns.values)
