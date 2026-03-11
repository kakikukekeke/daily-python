%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(font=["Meiryo","Yu Gothic"])


df = pd.read_csv("cake_survey.csv",encoding="utf-8")

#sns.boxenplot(data=df,width=0.2)
df.plot.scatter(x="参加者番号",y="A案",c="b",figsize=(12,8))

x = df.iloc[3]["参加者番号"]
y = df.iloc[3]["A案"]
plt.plot(x,y,c="r",marker="X",markersize=15)
plt.axvline(x=x,c="r",linestyle="--")
plt.axhline(y=y,c="r",linestyle="--")
plt.show()


print(df.median())
