import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    "Math_Score": [85, 62, 78, 50, 88],
    "English_Score": [90, 72, 80, 60, 95],
}

df = pd.DataFrame(data)
high_Score = df[(df['Math_Score'] > 70) & (df['English_Score'] > 70)]
math_descending = df.sort_values("Math_Score", ascending=False)

print(df)
print("-----")
print(high_Score)
print("-----")
print(math_descending)
print("-----")
print(df["Name"])