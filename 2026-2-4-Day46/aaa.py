import pandas as pd
import openpyxl

df = pd.read_excel("test.xlsx")
print(df)
df = pd.read_excel("test.xlsx",sheet_name="aaa")
print(df)
