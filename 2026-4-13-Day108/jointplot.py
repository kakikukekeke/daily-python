%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(font=["Yu Gothic"])

df = pd.read_csv("sample_data.csv")
df.head()
df.plot.scatter(x="order_id",y="discount_rate",c="b")
plt.show()
sns.regplot(data=df,x="order_id",y="discount_rate",line_kws={"color":"red"})
plt.show()
sns.jointplot(data=df,x="order_id",y="discount_rate",kind="reg",line_kws={"color":"red"})
plt.show()


print(df.corr(numeric_only=True)["order_id"]["discount_rate"])
