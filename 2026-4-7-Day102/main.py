import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
sns.set(font=["Meiryo","Yu Gothic"])

df = pd.DataFrame({
    "A":np.random.randint(0,100,15),
    "B":np.random.normal(50,10,15)
})

sns.histplot(df["A"],kde=False, stat="density",)
plt.title("偏りのないランダムな値")
plt.show()
sns.histplot(df["B"],kde=False,stat="density")
plt.title("世紀部分布になるようなランダムの値")

mu_b, std_b = norm.fit(df["B"])
x_b = np.linspace(df["B"].min(), df["B"].max(), 100)
plt.plot(x_b, norm.pdf(x_b, mu_b, std_b), color="red")
plt.show()
