import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Hiragino Maru Gothic Pro",
"Hiragino sans","BIZ UDGothic","MS Gothic"]

df = pd.read_csv("sample.csv")

df.plot.bar()
plt.legend(loc="lower right")
plt.show()

df.plot.barh()
plt.legend(loc="lower left")
plt.show()

df.plot.box()
plt.show()

df.plot.area()
plt.legend(loc="lower right")
plt.show()
