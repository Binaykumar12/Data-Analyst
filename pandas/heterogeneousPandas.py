import pandas as pd

# DataFrame with heterogeneous columns
df = pd.DataFrame({
    'Age': [25, 30, 35],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Salary': [50000.0, 60000.0, 70000.0]
})

# Series with mixed types (heterogeneous within the Series)
series = pd.Series([1, 'two', 3.0, True])

print(df)
print(series)
