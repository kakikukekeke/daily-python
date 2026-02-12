import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Hiragino Maru Gothic Pro",
"Hiragino sans" , "BIZ UDGothic","MS Gothic"]

df = pd.read_csv("population.csv",index_col=
                 "全国・都道府県",encoding="UTF-8")
df["2022年"] = pd.to_numeric(df["2022年"].str.replace(",",""))
print(df["2022年"])
df["2022年"].plot.bar()
plt.show()
