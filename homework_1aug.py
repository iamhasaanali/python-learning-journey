import pandas as pd
df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "age": [27, 22, 25, 30, 28],
    "salary": [70000, 45000, 65000, 80000, 55000],
    "years": [6, 3, 7, 8, 4]
})
print(df[:3])
print("--------------------")
def employee_level(row):
    if row["years"] > 5 and row["salary"] > 60000:
        return f"Senior"
    elif row["years"] > 2 and row["salary"] > 50000:
        return f"Mid"
    else:
        return f"Junior"

df["level"] = df.apply(employee_level, axis=1)
print(df)
print("--------------------")
senior = df[df["level"]=="Senior"]
print(senior)
print("--------------------")
print(df.sort_values("salary", ascending=False))