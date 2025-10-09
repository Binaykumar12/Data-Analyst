import pandas as pd

data = {
    "Name": ['Ram', 'Ramesh', 'Binay', 'Hari', 'Sita', 'Gita', 'Rita', 'Akriti'],
    "Age": [20, 25, 22, 30, 28, 31, 33, 34],
    "salary": [20000, 30000, 40000, 25000, 35000, 24000, 28000, 32000],
    "Performance Score": [80, 70, 90, 85, 88, 92, 82, 78]
}

df = pd.DataFrame(data)

single = df["Name"]
print("Single column: ")
print(single)

print("\nMultiple columns: ")
print(df[["Name", "salary"]])

