%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(font=["Meiryo","Yu Gothic"])


df = pd.read_csv("cake_survey.csv",encoding="utf-8")
df[["A案"]].plot.hist(bins=10)
bins = 10
df["A案"].plot.hist(bins=bins,color="c",ylim=(0.6))
plt.title("A baratuki")
plt.show()

df["B案"].plot.hist(bins=bins,color="c",ylim=(0.6))
plt.show()
