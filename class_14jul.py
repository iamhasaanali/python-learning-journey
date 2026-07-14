names = ["Hasaan", "Ali", "Sara", "Ahmed"]
grades = [85, 92, 78]

if len(names) == len(grades):
    combined = dict(zip(names, grades))
    print(combined)
else:
    print(f"Lists have different lengths! names={len(names)}, grades={len(grades)}")

#exercise 2 3 lists zip
names = ["Hasaan", "Ali", "Sara"]
grades = [85, 92, 78]
cities = ["Sydney", "Karachi", "London"]
for names,grades,cities in zip(names,grades,cities):
    print(f"{names} scored {grades} and live in {cities}")

#exercise 3 3 lists in dict
import pandas as pd
names = ["Hasaan", "Ali", "Sara"]
grades = [85, 92, 78]
cities = ["Sydney", "Karachi", "London"]
combined = [
    {"name": name, "grade": grade, "city": city}
    for name, grade, city in zip(names, grades, cities)
]
print(combined)
df = pd.DataFrame(combined)
print(df)

#exercise 4 
names = ["Hasaan", "Ali", "Sara"]
grades = [85, 92, 78]
cities = ["Sydney", "Karachi", "London"]
ages = [27, 22, 25]
departments = ["IT", "HR", "Finance"]
combined = [
    {"name" : name, "grade": grade, "city": city, "age": age, "department": department}
    for name,grade,city,age,department in zip(names,grades,cities,ages,departments)
]
df = pd.DataFrame(combined)
print(df)
print("---------------------------------------------------")
#exercis 5 test
import pandas as pd
names = ["Hasaan", "Ali", "Sara","Ahmad","Sharjeel"]
grades = [85, 92, 78, 98, 88]
cities = ["Sydney", "Karachi", "London", "Sydney", "Burewala"]
ages = [28, 22, 25, 26, 27]
if len(names)==len(grades)==len(cities)==len(ages):
    combined = [
        {"name" : name, "grade": grade, "city": city, "age": age}
        for name,grade,city,age in zip(names,grades,cities,ages)
    ]
    df = pd.DataFrame(combined)
    print(df)
else:
    print(f"Lists have different lengths! names={len(names)}, grades={len(grades)}, cities={len(cities)}, ages={len(ages)}")

df["calculated"] = df["grade"] * 0.2
print(df)
print("------")
passed = df[df["grade"] > 80]
print(passed)
print("------")
print(df.sort_values("grade", ascending=False).head(2))
print("------")
df.to_csv("/Users/hasaanali/Documents/My_Learning/class_14jul.csv", index=False)

new_df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/class_14jul.csv")
print(new_df)