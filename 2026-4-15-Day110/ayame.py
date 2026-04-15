%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set()

df = sns.load_dataset("iris")
df.head()
df.corr(numeric_only=True)
sns.heatmap(df.corr(numeric_only=True),annot=True,vmax=1,vmin=-1,center=0)
plt.show()
