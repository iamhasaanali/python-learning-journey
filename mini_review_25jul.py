import pandas as pd
employees = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed"],
    "dept_id": [1, 2, 1, 3],
    "salary": [70000, 45000, 65000, 80000]
})

departments = pd.DataFrame({
    "dept_id": [1, 2],
    "dept_name": ["IT", "HR"],
    "location": ["Sydney", "Karachi"]
})
merged = pd.merge(employees,departments, on="dept_id")
missing_dept = pd.merge(employees,departments, on="dept_id", how="left")
print(missing_dept)
print("------------------")
print(merged.pivot_table(values="salary", index="dept_name", aggfunc="mean"))
print("\n------------------")
#exercise 2
import pandas as pd
data = {
    "product": ["iPhone 17", "Samsung S25", "MacBook Pro", "iPad Air", "Surface Laptop"],
    "brand": ["Apple", "Samsung", "apple", "APPLE", "Microsoft"],
    "price": [2200, 1800, 3999, 1200, 1500]
}
df = pd.DataFrame(data)
print(df[df["brand"].str.contains("apple" , case=False)])
print("------------------")
print(df[df["product"].str.startswith("i")])
print("------------------")
print(df[(df["price"] > 1500) & (df["brand"].str.contains("apple", case=False))])
print("------------------")
df["brand"] = df["brand"].str.title()
print(df)
import pandas as pd
print("\n------------------")

#exercise 3
import pandas as pd
sales = pd.DataFrame({
    "salesperson": ["Hasaan", "Ali", "Sara", "Ahmed", "Hasaan", "Sara"],
    "region_id": [1, 2, 1, 3, 2, 1],
    "amount": [5000, 3000, 7000, 4000, 6000, 2000]
})

regions = pd.DataFrame({
    "region_id": [1, 2],
    "region_name": ["Sydney", "Karachi"],
    "target": [10000, 8000]
})
merged = pd.merge(sales,regions, on="region_id")
filtered = merged[merged["amount"] > 4000]
print(filtered)
print("------------------")
print(merged.pivot_table(values="amount", index="salesperson", aggfunc="sum"))
print("------------------")
print(merged.groupby("region_name")["amount"].sum())
