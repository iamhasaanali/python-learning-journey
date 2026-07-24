#exercise 1 merge()
import pandas as pd
employees = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "department": ["IT", "HR", "IT", "Finance", "Marketing"],
    "salary": [70000, 45000, 65000, 80000, 60000]
})

departments = pd.DataFrame({
    "department": ["IT", "HR", "Finance"],
    "location": ["Sydney", "Karachi", "London"],
    "budget": [500000, 300000, 400000]
})
print(employees)
print("-----------")
print(departments)
print("-----------")
merged = pd.merge(employees,departments, on="department")
print(merged)
print("-----------Merge Left")
merged_left = pd.merge(employees, departments, on="department", how="left")
print(merged_left)
print("-----------Merge Right")
merged_right = pd.merge(employees,departments, on="department", how="right")
print(merged_right)
print("-----------Merge Outer")
merged_outer = pd.merge(employees,departments, on="department", how="outer")
print(merged_outer)
print("\n-------------------------------")
#exercise 2 
import pandas as pd
students = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "course_id": [1, 2, 1, 3, 4],
    "grade": [85, 92, 78, 95, 88]
})

courses = pd.DataFrame({
    "course_id": [1, 2, 3],
    "course_name": ["Python", "Data Science", "Machine Learning"],
    "instructor": ["Mr. Khan", "Ms. Smith", "Mr. Ali"]
})
print(students)
print("-----------")
print(courses)
print("-----------")
merge = pd.merge(students,courses, on="course_id", how="inner")
print(merge)
print("-----------Left merge")
merge_left = pd.merge(students,courses, on="course_id", how="left")
print(merge_left)
print("\n-------------------------------")

#exercise 3 pivot_table()
import pandas as pd
df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "salary": [70000, 45000, 65000, 80000, 50000, 75000],
    "gender": ["M", "M", "F", "M", "F", "M"]
})
print(df.pivot_table(values="salary", index="department", aggfunc="mean"))
print("-----------")
print(df.pivot_table(values="salary", index="department", columns="gender", aggfunc="mean", fill_value=0))
print("-----------")
print(df.pivot_table(values="salary", index="department", aggfunc=["mean", "max", "min"]))
print("\n-------------------------------")

#exercise 4 independnt
import pandas as pd
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6],
    "customer": ["Hasaan", "Ali", "Sara", "Hasaan", "Sara", "Ahmed"],
    "product_id": [101, 102, 101, 103, 102, 101],
    "quantity": [2, 1, 3, 1, 2, 4],
    "amount": [200, 150, 300, 500, 300, 400]
})

products = pd.DataFrame({
    "product_id": [101, 102, 103],
    "product_name": ["Laptop Stand", "Mouse", "Keyboard"],
    "category": ["Accessories", "Accessories", "Accessories"]
})
print(orders)
print("-----------")
print(products)
print("-----------")
mergg = pd.merge(orders,products, on="product_id", how="inner")
print(mergg)
print("-----------")
print(mergg.pivot_table(values="amount", index="customer", columns="product_name", aggfunc="sum" , fill_value= 0))
print("-----------")
print(mergg.pivot_table(values="quantity", index="customer", aggfunc="mean"))
print("-----------")
filtered = mergg[mergg["amount"] > 250]
print(filtered)
print("-----------")
highest = mergg.groupby("customer")["amount"].sum().sort_values(ascending=False).head(1)
print(highest)