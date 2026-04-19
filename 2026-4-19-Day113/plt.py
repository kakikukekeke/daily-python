import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


df = pd.read_csv("money.csv",encoding="shift_jis")
sns.pairplot(data=df)
plt.show()

print(df.head())
