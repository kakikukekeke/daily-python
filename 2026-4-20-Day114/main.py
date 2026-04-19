import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


df = pd.read_csv("money.csv",encoding="shift_jis")
df["お取引日"] = pd.to_datetime(df["お取引日"])

daily_df = df.groupby("お取引日")["お取引金額"].sum().reset_index()

sns.pairplot(data=df)
plt.show()

print(df.head())
