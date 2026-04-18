%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set()
onespecies = "setosa"
df = sns.load_dataset("iris")
df.head()
one = df[df["species"]==onespecies]
sns.pairplot(data=df,hue="species")
plt.show()


df["species"].unique()
