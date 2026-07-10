#exercise 1
import pandas as pd

df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/students.csv")
print(df.groupby("city")["age"].mean())
print(df[df["grade"] > 80])
print(df.sort_values("grade", ascending=True).head(1))

print("---------------------------------------------------")

#exercise 2

import pandas as pd

df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/products.csv")
print("Shape:", df.shape)
print("-----")
print("Columns:",df.columns.tolist())
print("-----")
print(df.head(3))
print("-----")
print(df["category"].value_counts())
print("-----")
print(df.groupby("category")["price"].mean())

#exercise 3
countries = ["Australia", "Pakistan", "England", "UAE", "Canada"]
capitals = ["Canberra", "Islamabad", "London", "Abu Dhabi", "Ottawa"]
combined = zip(countries, capitals)
result = dict(combined)

for countries,capitals in result.items():
    print(f"The Capitl of {countries} is {capitals}")
