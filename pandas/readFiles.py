import pandas as pd

# df = pd.read_csv("files/sales_data_sample.csv", encoding="latin1")
# print(df.head(10))

df = pd.read_excel("files/SampleSuperstore.xlsx")
print(df)


df = pd.read_json("files/sample_Data.json")
print(df.info())
