import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("temp.csv",index_col=0,skiprows=1,
                  encoding="utf-8-sig")
df2 = pd.read_csv("top_temp.csv",index_col=0,skiprows=1,
                   encoding="utf-8-sig")
df3 = pd.read_csv("low_temp.csv",index_col=0,skiprows=1,
                   encoding="utf-8-sig")
df.columns = df.columns.str.strip()
df2.columns = df2.columns.str.strip()
df3.columns = df3.columns.str.strip()

print(df.columns.values)
df["年平均気温【℃】"].plot()
df2["東京都"].plot()
df3["東京都"].plot()
plt.ylim(-10,40)
plt.rcParams["font.family"] = "BIZ UDGothic"
plt.legend(loc="lower right")
plt.show()
print(df2.columns.values)
print(df3.columns.values)
