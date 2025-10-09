import pandas as pd

data = {
    "Name": ['Ram', 'Ramesh', 'Binay', 'Hari', 'Sita', 'Gita', 'Rita', 'Akriti'],
    "Age": [20, 25, 22, 30, 28, 31, 33, 34],
    "salary": [20000, 30000, 40000, 25000, 35000, 24000, 28000, 32000],
    "Performance Score": [80, 70, 90, 85, 88, 92, 82, 78]
}

df = pd.DataFrame(data)
print(df)

print("\nPerson with salary more than 30000: ")
print(df[df["salary"] > 30000])

print("\nPerson with salary more than 25000 and less than 35000:")
print(df[(df["salary"] > 25000) & (df["salary"] < 35000)])

print("\nPerson with age>25 and less than or equal to 33")
print(df[(df["Age"] > 25) & (df["Age"] <= 33)])


print("\nPerson with age>24 and salary<=32000")
print(df[(df["Age"] > 24) & (df["salary"] <= 32000)])

print("\n Person with age(>30+<34) or salary(<30000+>24000)")
print(df[((df["Age"] > 30) & (df["Age"]<34)) | ((df["salary"] < 30000) & (df["salary"]>24000))])


