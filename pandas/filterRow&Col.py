import pandas as pd

data = {
    "Name": ['Ram', 'Ramesh', 'Binay', 'Hari', 'Sita', 'Gita', 'Rita', 'Akriti'],
    "Age": [20, 25, 22, 30, 28, 31, 33, 34],
    "salary": [20000, 30000, 40000, 25000, 35000, 24000, 28000, 32000],
    "Performance Score": [80, 70, 90, 85, 88, 92, 82, 78]
}

df = pd.DataFrame(data)
print(df.dtypes)

print("\nMultiple condns:")
print(df[((df["Age"] > 30) & (df["Age"] < 34)) | (
    (df["salary"] < 30000) & (df["salary"] > 24000))])

print("\nselecting specific columns by filtering rows :")
print(df.loc[((df["Age"] > 30) & (df["Age"] < 34)) | (
    (df["salary"] < 30000) & (df["salary"] > 24000)), ["Name", "Age", "salary"]])


print("\nusing iloc: ")
print(df.iloc[2])

print("\nSelecting specific row element: ")
print(df.loc[df["Name"] == "Binay"])

print("\nSelecting specific row element: ")
print(df.loc[(df["Name"] == "Binay") | (df["Name"] == "Ramesh"),["Name","Performance Score"]])

print("\nFinding Gita's Performance Score: ")
print(df.loc[df["Name"]=="Gita",["Name","Performance Score"]])