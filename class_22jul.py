#exercise 1 groupby() multiple itemns
import pandas as pd
data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "salary": [70000, 45000, 65000, 80000, 50000, 75000],
    "age": [27, 32, 25, 35, 29, 31]
}
df = pd.DataFrame(data)
print(df.groupby("department")["salary"].agg(["mean", "sum", "count", "min", "max"]))
print("-----")
df["senior"] = df["age"] > 30
print(df.groupby(["department", "senior"])["salary"].mean())
print("-----")
print(df.groupby("department").agg({"salary" : ["mean", "max"], "age" :["mean", min]}))
print("-----")
result = df.groupby("department")["salary"].mean().reset_index()
print(result)
print(type(result))
print("\n-----------------------------")
#exercise 2 self #exercise 3 transform() groupby()

import pandas as pd
data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar", "Zara"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT"],
    "salary": [70000, 45000, 65000, 80000, 50000, 75000, 60000],
    "age": [27, 32, 25, 35, 29, 31, 28]
}
df = pd.DataFrame(data)
df["senior"] = df["age"] > 30
result = df.groupby("department")["salary"].agg(["mean", "max", "min"]).reset_index()
print(result.sort_values("mean", ascending=False))
print("------")
high_salary = result[result["mean"] > 60000]
print(high_salary)
print("-------")
df["dep_avg_salary"] = df.groupby("department")["salary"].transform("mean")
print(df[["name", "department", "salary", "dep_avg_salary"]])
print("------")
df["above_avg"] = df["salary"] > df["dep_avg_salary"]
print(df[["name", "department", "salary", "dep_avg_salary", "above_avg"]])
