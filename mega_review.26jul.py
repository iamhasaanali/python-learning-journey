#exercise 1
import pandas as pd
data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "salary": [70000, 45000, 65000, 80000, 50000, 75000]
}

df = pd.DataFrame(data)
df["dept_avg"] = df.groupby("department")["salary"].transform("mean")
df["above_avg"] = df["salary"] > df["dept_avg"]
print(df)


print("\n-----Exercise 2-----")
#ecercise 2
import pandas as pd
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "customer": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "product_id": [101, 102, 103, 101, 104],
    "amount": [500, 300, 700, 200, 400]
})

products = pd.DataFrame({
    "product_id": [101, 102, 103],
    "product_name": ["Laptop", "Mouse", "Keyboard"],
    "category": ["Electronics", "Accessories", "Accessories"]
})
merged = pd.merge(orders,products, on="product_id")
valid_pd = pd.merge(orders,products, on="product_id", how="inner")
missing_pd = pd.merge(orders,products, on="product_id", how="left")
print(valid_pd)
print("----------")
print(missing_pd)

print("\n-----Exercise 3-----")
#exercise 3
#data from exercise 2 inner merge
print(valid_pd.pivot_table(values="amount", index="customer", columns="category" ,aggfunc="sum" , fill_value=0))

print("\n-----Exercise 4-----")
#exercise 4
import pandas as pd
data = {
    "name": ["hasaan ali", "ALI KHAN", "Sara Ahmed", "ahmed raza", "FATIMA"],
    "city": ["Sydney", "karachi", "LONDON", "dubai", "Melbourne"],
    "score": [85, 92, 78, 68, 95]
}
df = pd.DataFrame(data)
df["name"] = df["name"].str.title()
df["city"] = df["city"].str.title()
cities_a = df[df["city"].str.contains("a", case=False)]
long_names = df[df["name"].str.len() > 8]
print(long_names)
print("----------")
print(cities_a)

print("\n-----Exercise 5-----")
#exercise 5
import pandas as pd
names = ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"]
departments = ["IT", "HR", "IT", "Finance", "HR"]
salaries = [70000, 45000, 65000, 80000, 55000]
ages = [27, 32, 25, 35, 29]
if len(names)==len(departments)==len(salaries)==len(ages):
    combine = [
        {"name": name, "department": department, "salary": salary, "age": age}
        for name,department,salary,age in zip(names,departments,salaries,ages)
    ]
else:
    ("lengths doesnt match")
df = pd.DataFrame(combine)
df["senior"] = df["age"] > 30
print(df[df["senior"]])
print("----------")
print(df)


print("\n-----Exercise 6-----")
#exercise 6
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
people = [
    {"name": "Hasaan", "birthday": datetime(1998, 7, 6)},
    {"name": "Ali", "birthday": datetime(2001, 3, 15)},
    {"name": "Sara", "birthday": datetime(1995, 11, 22)},
    {"name": "Ahmed", "birthday": datetime(2000, 8, 10)},
]
for person in people:
    diff = relativedelta(today,person["birthday"])
    person["age"] = diff.years
    print(f"{person["name"]} is {person["age"]} years old")
print("----------")
oldest = max(people, key=lambda x: x["age"])
youngest = min(people, key=lambda x: x["age"])
print(f"{oldest["name"]} is oldest in list")
print("----------")
print(f"{youngest["name"]} is youngest in list")
print("----------")
df = pd.DataFrame(people)
print(df.sort_values("age" ,ascending=False))


print("\n-----Exercise 7-----")
#exercise 7
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
        diff= relativedelta (today,self.start_date)
        return diff.years
    def is_senior(self):
        if self.years_worked() > 3:
            return True
        else:
            return False
    def display(self):
        print(f"name : {self.name}, department: {self.department}, salary: {self.salary}, years worked: {self.years_worked()}, senior: {self.is_senior()}")

e1 = Employee("Hasaan", "IT", 70000, datetime(2020, 3, 15))
e2 = Employee("Ali", "HR", 45000, datetime(2022, 7, 1))
e3 = Employee("Sara", "Finance", 65000, datetime(2019, 11, 20))

employees = [e1, e2, e3]
for e in employees:
    e.display()
    
print("\n-----Exercise 8-----")
#exercise 8
import pandas as pd
data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar", "Zara"],
    "city": ["Sydney", "Karachi", "Sydney", "London", "Karachi", "London", "Sydney"],
    "score": [85, 72, 91, 68, 78, 95, 88],
    "age": [27, 22, 25, 30, 28, 26, 24]
}
df = pd.DataFrame(data)
filtered = (df.groupby("city")["score"].agg(["mean","max","min"]).reset_index())
print(filtered)
print("----------")
sorted = filtered.sort_values("mean", ascending=False)
print(sorted)
print("----------")
print(filtered[filtered["mean"] >80])

print("\n-----Exercise 9-----")
#exercise 9
players = [
    ("Babar Azam", 58.3, "Pakistan"),
    ("Virat Kohli", 53.6, "India"),
    ("Steve Smith", 61.8, "Australia"),
    ("Joe Root", 50.2, "England"),
    ("Kane Williamson", 54.7, "New Zealand")
]
for player in players:
    print(f"{player[0]} — Average: {player[1]} — Country: {player[2]}")
print("----------")
highest_avg = max(players, key=lambda x: x[1])
print(f"{highest_avg[0]} has highest average and he is from {highest_avg[2]}")
print("----------")
lowest_avg = min(players, key=lambda x: x[1])
print(f"{lowest_avg[0]} has the lowest average of all")
print("----------")
players.sort(key=lambda x: x[1], reverse=True)
for player in players[:3]:
    print(f"{player[0]}: {player[1]}")

print("\n-----Exercise 10-----")
#exercise 10
import pandas as pd
data = {
    "product": ["iPhone 17 Pro", "samsung galaxy", "MacBook Air", "IPAD MINI", "surface pro"],
    "brand": ["Apple", "samsung", "Apple", "APPLE", "Microsoft"],
    "price": [2500, 1200, 1800, 900, 1500],
    "stock": [50, 30, 25, 60, 40]
}

df = pd.DataFrame(data)
df["product"] = df["product"].str.title()
df["brand"] = df["brand"].str.title()
print(df[df["product"].str.contains("pro", case=False)])
print("----------")
apple = df[(df["brand"] == "Apple") & (df["price"] > 1500)]
print(apple)
print("----------")
df["discounted"] = (df["price"] * 0.85).round(2)
print(df)

print("\n-----Exercise 12-----")
#exercise 12 exercise 11 is in daily_goals.py file
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

employees = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "dept_id": [1, 2, 1, 3, 2],
    "salary": [70000, 45000, 65000, 80000, 55000],
    "start_date": [
        datetime(2020, 3, 15),
        datetime(2022, 7, 1),
        datetime(2019, 11, 20),
        datetime(2018, 5, 10),
        datetime(2021, 9, 5)
    ]
})

departments = pd.DataFrame({
    "dept_id": [1, 2],
    "dept_name": ["IT", "HR"],
    "location": ["Sydney", "Karachi"]
})
merg = pd.merge(employees,departments, on="dept_id", how="left")
def get_years(start_date):
    diff = relativedelta(datetime.now(), start_date)
    return diff.years

merg["years_worked"] = merg["start_date"].apply(get_years)
print(merg)
merg["dept_avg"] = merg.groupby("dept_name")["salary"].transform("mean")
merg["above_avg"] = merg["salary"] > merg["dept_avg"]
print("----------")
print(merg)
print("----------")
print(merg.groupby("dept_name")["salary"].agg(["mean", "max"]).reset_index())

