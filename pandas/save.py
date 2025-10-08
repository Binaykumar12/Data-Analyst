import pandas as pd

data = {
    "Name": ["Ram", "Hari", "Binay", "Sita"],
    "Age": [10, 20, 30, 40],
    "city": ["UK", "USA", "NP", "IND"]
}

df = pd.DataFrame(data)
print(df.info())

# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
# df.to_json("output.json", index=False)
