%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set()
onespecies = "setosa"
df = sns.load_dataset("iris")
df.head()
one = df[df["species"]==onespecies]
sns.heatmap(one.corr(numeric_only=True),annot=True,vmax=1,vmin=-1,center=0)
plt.show()
df.corr(numeric_only=True)


df["species"].unique()
