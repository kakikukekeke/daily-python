%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(font=["Meiryo","Yu Gothic"])


df = pd.read_csv("cake_survey.csv",encoding="utf-8")

#sns.boxenplot(data=df,width=0.2)
df.plot.scatter(x="参加者番号",y="A案",c="b",ylim=(0,100))

plt.axhline(y=50,c="Magenta")
plt.show()
print(df.var())

print(df.median())
