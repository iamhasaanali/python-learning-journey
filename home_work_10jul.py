#exercise 1
import pandas as pd

data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar", "Zara"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT"],
    "salary": [70000, 45000, 65000, 80000, 50000, 75000, 60000]
}

df = pd.DataFrame(data)
print(df.groupby("department")["salary"].mean())

#exercise 2
import pandas as pd

data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "age": [27, None, 25, None, 28],
    "salary": [70000, 45000, None, 85000, 55000],
    "department": ["IT", "HR", None, "Finance", "IT"]
}

df = pd.DataFrame(data)
print(df)
print(df.isnull().sum())
df["age"] = df["age"].fillna(df["age"].mean())
df["department"] = df["department"].fillna("Umknown")
print(df)
df = df.dropna(subset=["salary"])
print(df)

#exercise 3
class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def is_passing(self):
        return self.grade >= 50
    
s1 = student("Hasaan", 98)
s2 = student("Ahmad", 78)
s3 = student("Sharjeel", 67)
s4 = student("Sara", 44)
print(s1.name, "passed: ", s1.is_passing())
print(s4.name, "passed: ", s4.is_passing())