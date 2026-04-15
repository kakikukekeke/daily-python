%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(font=["Yu Gothic"])

df = pd.read_csv("sample_data.csv")
sns.pairplot(data=df,kind="reg")
plt.show()




print(df.corr(numeric_only=True)["order_id"]["discount_rate"])
