import pandas as pd
import openpyxl

df = pd.read_csv("sample.csv" , index_col=0)

kokugo = df.sort_values("japanease",ascending=False)

kokugo.to_excel("test.xlsx",index=False,sheet_name="aaa")


