import pandas as pd 
df = pd.read_csv("watar.csv",encoding="shift-jis")

hydrant = df[["緯度","経度"]].values
print(len(hydrant))
print(hydrant)
