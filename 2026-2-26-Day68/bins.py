import pandas as pd
df = pd.read_csv("cake_survey.csv")

bins = [1,3,5,7,9,11]
cut = pd.cut(df["A案"],bins=bins,right=False)
cut.value_counts(sort=False)
