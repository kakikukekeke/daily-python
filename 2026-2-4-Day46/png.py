import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Hiragino Maru Gothic Pro",
"Hiragino sans","BIZ UDGothic","MS Gothic"]

df = pd.read_csv("sample.csv" , index_col=0)

colorlist = ["skyblue","steelblue","tomato","cadetblue",
             "orange","sienna"]
df.T.plot.bar(color=colorlist)
plt.legend(loc="lower left")
plt.savefig("test.png")
