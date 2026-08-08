import numpy as np

scores = np.array([85, 92, 45, 78, 95, 62, 88, 71, 55, 90])

print(np.sum(scores))
print(np.mean(scores))
print(np.max(scores))
print(np.min(scores))
print(scores[scores > 75])
print(scores * 1.05)
print(np.sort(scores)[::-1])
print(np.sort(scores)[::-1][:3])

print("\n------exercise 2------")
#exercise 2
import pandas as pd

df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar"],
    "salary": [70000, 45000, 65000, 80000, 55000, 75000],
    "score": [85, 72, 91, 68, 78, 95]
})
print(df.loc[df["salary"].idxmax()])
print(df.loc[df["score"].idxmin()])
print(df.iloc[1:4])
print(df.loc[2:4])

print("\n------exercise 3------")
#exercise 3
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Employee:
    def __init__(self,name,department,salary,start_date):
        self.name = name
        self.department = department
        self.salary = salary
        self.start_date = start_date
    def years_worked(self):
        today = datetime.now()
        diff = relativedelta(today,self.start_date)
        return diff.years
    def is_senior(self):
        if self.years_worked() > 4:
            return True
        else:
            return False
    def bonus(self):
        if self.is_senior():
            return self.salary * 1.15
        else:
            return self.salary * 1.05

e1 = Employee("Hasaan", "IT", 70000, datetime(2020, 3, 15))
e2 = Employee("Ali", "HR", 45000, datetime(2023, 7, 1))
e3 = Employee("Sara", "IT", 65000, datetime(2018, 11, 20))
employees = [e1,e2,e3]
data = []
for e in employees:
    data.append({
        "name": e.name,
        "department": e.department,
        "salary": e.salary,
        "years_worked": e.years_worked(),
        "is_senior": e.is_senior(),
        "bonus": e.bonus()
    })

df = pd.DataFrame(data)
print(df)

print("\n------exercise 4------")
#exercise 4
import pandas as pd
import numpy as np
data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "math": [85, 42, 91, 68, 78],
    "english": [78, 65, 88, 72, 45],
    "science": [90, 55, 85, 68, 82]
}

df = pd.DataFrame(data)

print(np.mean(df["math"]))
print(np.max(df["english"]))
df["total"] = df["math"] + df["english"] + df["science"]
df["average"] = df["total"] / 3
print(df)
print(df.loc[df["average"].idxmax()])

print("\n------exercise 5------")
#exercise 5
import pandas as pd
import numpy as np
data = {
    "product": ["iPhone", "Samsung", "MacBook", "iPad", "Surface"],
    "brand": ["apple", "SAMSUNG", "Apple", "APPLE", "microsoft"],
    "price": [2200, 1800, 3999, 900, 1500],
    "stock": [50, 30, 25, 60, 40]
}

df = pd.DataFrame(data)

df["brand"] = df["brand"].str.title()
print(df[df["brand"] == "Apple"])
print("-------------------------------")
print(np.mean(df["price"]))
print("-------------------------------")
df["discount"] = df["price"] * 0.85
print(df.loc[df["price"].idxmax()])
print("-------------------------------")
print(df.sort_values("price", ascending=False))
print("-------------------------------")
print(df)