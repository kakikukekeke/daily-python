
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font=["MeiryoF","Yu Gothic","Hiragino Maru Gothic Pro"])

def galton(steps,count):
    ans = []

    for i in range(count):
        val = 50
        for j in range(steps):
            if random.randint(0,1) == 0:
                val -= 1
            else:
                val += 1
        ans.append(val)

    df = pd.DataFrame(ans)
    df[0].plot.hist()
    plt.ylabel("")
    plt.show()

galton(1,10000)
