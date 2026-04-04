import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"])

df = pd.DataFrame({
    "A":np.random.randint(0,100,15),
    "B":np.random.normal(50,10,15)
})

sns.distplot(df["A"],fit=norm,fit_kws={"color":"red"})
plt.title("偏りのないランダムな値")
plt.show()
sns.distplot(df["B"],fit=norm,fit_kws={"color":"red"})
plt.title("世紀部分布になるようなランダムの値")
plt.show()
