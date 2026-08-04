print("\n------exercise 1------")
#exercise 1
import pandas as pd
df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara"],
    "salary": [70000, 45000, 65000]
}, index=[10, 20, 30])
print("-------------------------------")
print(df.iloc[0])
print("-------------------------------")
print(df.loc[10])
print("-------------------------------")
print(df.loc[20])
print("-------------------------------")

print("\n------exercise 2------")
#exercise 2
import pandas as pd

df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "salary": [70000, 45000, 65000, 80000, 55000]
})

# With normal index (0,1,2,3,4):
print(df.iloc[0])   # first row by position
print("---")
print(df.loc[0])    # row with label 0 — same result!
print("---")
print(df.iloc[2:4]) # rows at position 2 and 3
print("---")
print(df.loc[2:4])  # rows with labels 2, 3, 4 ← includes 4!
print("-------------------------------")

print("\n------exercise 3------")
#exercise 3
import pandas as pd
df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "salary": [70000, 45000, 65000, 80000, 55000]
})
idx = df["salary"].idxmax()
print(df.loc[idx])
print("-------------------------------")
print(F"Index of highest salary is: {idx}")
print("-------------------------------")
idx_min = df["salary"].idxmin()
print(F"Index of lowest salary is: {idx_min}")
print("-------------------------------")
print(df.loc[idx_min])

print("\n------exercise 4------")
#exercise 4
import pandas as pd

df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "score": [85, 92, 78, 95, 68],
    "salary": [70000, 45000, 65000, 80000, 55000]
})
print(df.loc[df["score"].idxmax()])
print("-------------------------------")
print(df.loc[df["score"].idxmin()])
print("-------------------------------")
print(df.iloc[1:4])
print("-------------------------------")
print(df.loc[2:4])
