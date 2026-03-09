%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(font=["Meiryo","Yu Gothic"])


df = pd.read_csv("cake_survey.csv",encoding="utf-8")

df["A案"].plot.pie(startangle=90,counterclock=False,labeldistance=0.5)
plt.xlabel("参加者")
plt.ylabel("評価点")
plt.title("How to feel tasete of cake")
plt.show()
