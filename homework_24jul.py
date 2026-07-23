#exercise 1
print("\n------Exercise 1------")
import pandas as pd

data = {
    "name": ["hasaan", "ALI", "Sara ", " ahmed", "FATIMA"],
    "city": ["  sydney", "karachi  ", "LONDON", " dubai  ", "melbourne"],
    "country": ["Australia", "pakistan", "England", "UAE", "australia"]
}
df = pd.DataFrame(data)
df["name"] = df["name"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()
df["country"] = df["country"].str.title()
print(df[df["city"].str.contains("a", case=False)])
print("--------")
print(df[df["name"].str.len() > 4])
print("---------")
print(df)

print("\n------Exercise 2------")
#exercise 2
import pandas as pd
names = ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"]
departments = ["IT", "HR", "IT", "Finance", "HR"]
salaries = [70000, 45000, 65000, 80000, 55000]
ages = [27, 32, 25, 35, 29]
if len(names)==len(departments)==len(salaries)==len(ages):
    combined = [
        {"name" : name, "department" : department, "salary" : salary, "age" : age}
        for name,department,salary,age in zip(names,departments,salaries,ages)
    ]
else:
    print("lengths doesnt match")
print("---------")
df = pd.DataFrame(combined)
df["senior"] = df["age"] > 30
result = df.groupby("department")["salary"].agg(["mean","max"]).reset_index()
print(result[result["mean"] > 55000])
print("---------")
print(result.sort_values("mean", ascending=False))
print("---------")
df.to_csv("/Users/hasaanali/Documents/My_Learning/pipeline_exercise.csv", index=False)

new_df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/pipeline_exercise.csv")
print(new_df)

print("\n------Exercise 3------")
#exercise 3
import pandas as pd
data = {
    "product": ["iPhone 17", "Samsung S25", "MacBook Pro", "AirPods", "Surface Pro", "iPad Mini"],
    "brand": ["Apple", "Samsung", "Apple", "Apple", "Microsoft", "Apple"],
    "price": [2200, 1800, 3999, 350, 1500, 800],
    "review": ["Great product love it!", "poor quality very bad", "Amazing value for money",
               "decent product okay", "Great build quality!", "poor battery life"]
}
df = pd.DataFrame(data)
print(df[df["review"].str.contains("great|amazing", case=False)])
print("---------")
expensive = df[(df["price"] > 500) & (df["review"].str.contains("great|amazing", case=False))]
print("---------")
print(expensive)
print("---------")
df["discount_price"] = (df["price"] * 0.9).round(2)
print(df.sort_values("price",ascending=False))