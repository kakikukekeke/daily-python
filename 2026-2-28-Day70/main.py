%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"])


df = pd.read_csv("cake_survey.csv")
plt.plot(df)
