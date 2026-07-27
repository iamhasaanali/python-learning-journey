#exercise 1
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Person:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday
    def age(self):
        today = datetime.now()
        diff = relativedelta(today,self.birthday)
        return diff.years
    def greeting(self):
        return f"Hi i am {self.name} and i am {self.age()} years old!"

p1 = Person("Hasaan", datetime(1998, 7, 6))
p2 = Person("Ali", datetime(2001, 3, 15))

print(p1.greeting())
print(p2.greeting())

print("\n-----Exercise 2-----")
#exercise 2
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Subscription:
    def __init__ (self,customer_name,start_date,price_per_month):
        self.customer_name = customer_name
        self.start_date = start_date
        self.price_per_month = price_per_month
    def months_active(self):
        today = datetime.now()
        diff = relativedelta(today,self.start_date)
        return diff.years * 12 + diff.months
    def total_paid(self):
        return self.months_active() * self.price_per_month
    def is_long_term(self):
        if self.months_active() > 6:
            return True
        else:
            return False
    def summary(self):
        return f"Name: {self.customer_name}, Active Subscription: {self.months_active()} months, Long term: {self.is_long_term()}, Total Paid: {self.total_paid()}"

s1 = Subscription("Hasaan", datetime(2025, 1, 1), 50)
s2 = Subscription("Ali", datetime(2026, 5, 1), 30)
s3 = Subscription("Sara", datetime(2024, 6, 1), 100)

print(s1.summary())
print(s2.summary())
print(s3.summary())

print("\n-----Exercise 3-----")
#exercise
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Product:
    def __init__(self,name,category,price,launch_date):
        self.name = name
        self.category = category
        self.price = price
        self.launch_date = launch_date
    def age_months(self):
        today = datetime.now()
        diff = relativedelta(today,self.launch_date)
        return diff.years * 12 + diff.months
    def is_new(self):
        if self.age_months() < 6:
            return True
        else:
            return False
    def discounted_price(self):
        if self.age_months() > 12:
            return self.price * 0.9
        else:
            return f"Not available"
    def summary(self):
        print(f"Name: {self.name}, launched: {self.age_months()} months ago,Original Price: {self.price}, Discount: {self.discounted_price()} ")


products = [
    Product("iPhone 17", "Electronics", 2200, datetime(2025, 9, 1)),
    Product("MacBook Pro", "Electronics", 3999, datetime(2024, 1, 1)),
    Product("AirPods", "Accessories", 350, datetime(2026, 5, 1)),
    Product("iPad Mini", "Tablets", 800, datetime(2023, 10, 1)),
]
for p in products:
    p.summary()
print("------------------")
data = []
for p in products:
    data.append({
        "name": p.name,
        "category": p.category,
        "price": p.price,
        "age_months": p.age_months(),
        "is_new": p.is_new(),
        "discounted_price": p.discounted_price()
    })
df = pd.DataFrame(data)
print(df)
print("----------")
print(df.sort_values("price", ascending=False))

print("\n-----Exercise 4-----")
#exercise 4
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Employee:
    def __init__ (self,name,department,salary,hire_date):
        self.name = name
        self.department = department
        self.salary = salary
        self.hire_date = hire_date
    def years_employed(self):
        today = datetime.now()
        diff = relativedelta(today,self.hire_date)
        return diff.years
    def months_employed (self):
        today = datetime.now()
        diff = relativedelta(today,self.months_employed)
        return diff.years * 12 + diff.months
    def annual_bonus(self):
        if self.years_employed() > 5:
            return self.salary * 0.15
        elif self.years_employed() > 2:
            return self.salary * 0.10
        else:
            return self.salary * 0.05
    def summary(self):
        return f"{self.name} | {self.department} | Salary: ${self.salary} | Years: {self.years_employed()} | Bonus: ${self.annual_bonus()}"

e1 = Employee("Hasaan", "IT", 70000, datetime(2020, 3, 15))
e2 = Employee("Ali", "HR", 45000, datetime(2022, 7, 1))
e3 = Employee("Sara", "IT", 65000, datetime(2019, 11, 20))
e4 = Employee("Ahmed", "Finance", 80000, datetime(2018, 5, 10))
e5 = Employee("Fatima", "HR", 55000, datetime(2021, 9, 5))

employees = [e1, e2, e3, e4, e5]
data = []
for e in employees:
    data.append({
        "name": e.name,
        "department": e.department,
        "salary": e.salary,
        "years": e.years_employed(),
        "bonus": e.annual_bonus() 
    })
df = pd.DataFrame(data)
print(df)
print("----------")
print(df.groupby("department")["bonus"].mean())
print("----------")
print(df.sort_values("salary", ascending=False))