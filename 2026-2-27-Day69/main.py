%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("cake_survey.csv")
plt.plot(df)

plt.show()
