%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(font=["Yu Gothic"])

df = pd.read_csv("sample_data.csv")
df.head()
df.plot.scatter(x="quantity",y="unit_price",c="discount_rate")
plt.show()

#df.plot.scatter(x="数学",y="社会",c="b")
#plt.show()
