print("\n------exercise 1------")
#exercise 1
import pandas as pd
df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "salary": [70000, 45000, 65000, 80000, 55000, 75000],
    "score": [85, 72, 91, 68, 78, 95]
})
print(df.loc[df["salary"].idxmax()])
print("-------------------------------")
print(df.loc[df["salary"].idxmin()])
print("-------------------------------")
print(df.iloc[0:4])
print("-------------------------------")
print(df.loc[2:5])


print("\n------exercise 2------")
#exercise 2
import pandas as pd

df = pd.DataFrame({
    "city": ["Sydney", "Karachi", "London", "Dubai", "Melbourne"],
    "population": [5000000, 15000000, 9000000, 3000000, 5000000],
    "avg_temp": [22, 28, 12, 35, 18]
})
print(df.loc[df["avg_temp"].idxmax()])
print("-------------------------------")
print(df.loc[df["population"].idxmin()])
print("-------------------------------")
print(df.iloc[-3:])
print("-------------------------------")
print(df.loc[1:3])


print("\n------exercise 3------")
#exercise 3
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Student:
    def __init__ (self,name,grade,enrollment_date):
        self.name = name
        self.grade = grade
        self.enrollment_date = enrollment_date
    def years_enrolled(self):
        today = datetime.now()
        diff = relativedelta(today,self.enrollment_date)
        return diff.years
    def is_senior(self):
        if self.years_enrolled() > 2:
            return True
        else:
            return False
    def summary(self):
        return f"{self.name} | Grade: {self.grade} | Years Enrolled: {self.years_enrolled()} | Senior: {self.is_senior()}"

s1 = Student("Hasaan", "A", datetime(2023, 3, 1))
s2 = Student("Ali", "B", datetime(2024, 7, 1))
s3 = Student("Sara", "A", datetime(2022, 1, 15))

students = [s1, s2, s3]
data = []
for s in students:
    data.append({
        "name": s.name,
        "grade": s.grade,
        "years_enrolled": s.years_enrolled(),
        "is_senior": s.is_senior()
    })

df = pd.DataFrame(data)
print(df)


print("\n------exercise 4------")
#exercise 4
import pandas as pd

employees = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "dept_id": [1, 2, 1, 3, 2],
    "salary": [70000, 45000, 65000, 80000, 55000]
})

departments = pd.DataFrame({
    "dept_id": [1, 2],
    "dept_name": ["IT", "HR"],
    "location": ["Sydney", "Karachi"]
})
merged = pd.merge(employees,departments, on = "dept_id", how= "left")
print(merged.loc[merged["salary"].idxmax()])
print("-------------------------------")
print(merged.groupby("dept_name")["salary"].mean())
print("-------------------------------")
print(merged)
