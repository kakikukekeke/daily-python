import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Hiragino Maru Gothic Pro",
"Hiragino sans","BIZ UDGothic","MS Gothic"]

df = pd.read_csv("sample.csv" , index_col=0)

df["japanease"].plot.barh()
plt.legend(loc="lower left")
plt.show()

df[["japanease","math"]].plot.barh()
plt.legend(loc="lower left")
plt.show()

df.loc["taito"].plot.barh()
plt.legend(loc="lower left")
plt.show()

df.loc["taito"].plot.pie(labeldistance=0.6)
plt.legend(loc="lower left")
plt.show()
