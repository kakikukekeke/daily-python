%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(font=["Meiryo","Yu Gothic"])


df = pd.read_csv("cake_survey.csv",encoding="utf-8")

df.plot.scatter(x="ID",y="A",color="b",ylim=(0,100))
plt.axhline(y=50, c="Magenta")
plt.show()
