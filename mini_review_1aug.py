print("\n------exercise 1------")
import pandas as pd
df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "score": [85, 42, 91, 68, 78]
})
def get_grade(score):
    if score >= 90:
        return f"A"
    elif score >= 80:
        return f"B"
    elif score >= 70:
        return f"C"
    else:
        return f"F"

df["grade"] = df["score"].apply(get_grade)
print(df)
print("--------------------")
print(df[-3:])

print("\n------exercise 2------")
#exercise 2
import pandas as pd
df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "math": [85, 42, 91, 55, 78],
    "english": [78, 65, 88, 72, 45],
    "science": [90, 55, 85, 68, 82]
})
def student_status(row):
    if row["math"] > 80 and row["english"] > 80 and row["science"] > 80:
        return f"Distinction"
    elif row["math"] > 60 and row["english"] > 60 and row["science"] > 60:
        return f"Pass"
    else:
        return f"Fail"
df["status"] = df.apply(student_status, axis=1)
print(df)
print("--------------------")
distincion_st = df[df["status"] == "Distinction"]
print(distincion_st)

print("\n------exercise 3------")
#exercise 3
from datetime import datetime
from dateutil.relativedelta import relativedelta
class Book:
    def __init__(self,title,author,publish_date,price):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.price = price
    def age_years(self):
        today = datetime.now()
        diff = relativedelta(today,self.publish_date)
        return diff.years
    def is_classic(self):
        if self.age_years() > 15:
            return True
        else:
            return False
    def discounted_price(self):
        if self.is_classic():
            return self.price * 0.8
        else:
            return f"No Discount Available"
    def summary(self):
        return f"{self.title} by {self.author} — {self.age_years()} years old — Classic: {self.is_classic()} — Price: ${self.discounted_price()}"

b1 = Book("The Alchemist", "Paulo Coelho", datetime(1988, 1, 1), 25)
b2 = Book("Atomic Habits", "James Clear", datetime(2018, 10, 16), 30)
b3 = Book("Sapiens", "Yuval Harari", datetime(2011, 1, 1), 35)
books = [b1,b2,b3]
for b in books:
    print(b.summary())

print("--------------------")
data = []
for book in books:
    data.append({
        "title" : book.title,
        "author" : book.author,
        "publish_date" : book.publish_date,
        "price" : book.price,
        "discount" :book.discounted_price(),
        "is_classic" : book.is_classic()
    })

df = pd.DataFrame(data)
print(df)

print("\n------exercise 4------")
#exercise 4
import pandas as pd

orders = pd.DataFrame({
    "customer": ["Hasaan", "Ali", "Sara", "Hasaan", "Ali"],
    "product_id": [1, 2, 1, 3, 1],
    "amount": [500, 300, 700, 200, 400]
})

products = pd.DataFrame({
    "product_id": [1, 2, 3],
    "product_name": ["Laptop", "Mouse", "Keyboard"],
    "category": ["Electronics", "Accessories", "Electronics"]
})

merge = pd.merge(orders,products, on="product_id", how="inner")
print(merge)
print("--------------------")
print(merge.groupby("customer")["amount"].sum())
print("--------------------")
print(merge.groupby("category")["amount"].mean())

print("\n------exercise 5------")
#exercise 5
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

employees = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "dept_id": [1, 2, 1, 2, 3],
    "salary": [70000, 45000, 65000, 50000, 80000],
    "hire_date": [
        datetime(2019, 3, 15),
        datetime(2022, 7, 1),
        datetime(2018, 11, 20),
        datetime(2021, 5, 10),
        datetime(2017, 9, 5)
    ]
})

departments = pd.DataFrame({
    "dept_id": [1, 2],
    "dept_name": ["IT", "HR"],
})
merged = pd.merge(employees,departments, on="dept_id", how="left")
print(merged)
print("--------------------")
def years_worked(row):
    today = datetime.now()
    diff = relativedelta(today,row["hire_date"])
    return diff.years

merged["years_worked"] = merged.apply(years_worked, axis=1)
print(merged)
print("--------------------")
def level(row):
    if row["years_worked"] > 6:
        return f"Senior"
    elif row["years_worked"] > 3:
        return f"Mid"
    else:
        return f"Junior"
merged["level"] = merged.apply(level,axis=1)
print(merged)
print("--------------------")
print(merged.groupby("dept_name")["salary"].mean())
print("--------------------")
senior_em = merged[merged["level"] == "Senior"]
print(senior_em)
