import pandas as pd

df = pd.read_csv("files/sales_data_sample.csv", encoding="latin1")
print(df.head())  # just to check it loaded correctly
