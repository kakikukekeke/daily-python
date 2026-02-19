import pandas as pd
df = pd.read_csv("sample.csv",index_col=0)
list_1 = [i for i in df.columns]
print(list_1)
list_2 = [i for i in df.index]
print(list_2)
