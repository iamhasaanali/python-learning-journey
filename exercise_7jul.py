#Exercise 1

subjects = ["Math", "Science", "English", "History"]
grades = [85, 92, 78, 88]
combined = zip(subjects,grades)
result = dict(combined)
print(result)

for subject, grade in result.items():
    print(f"{subject}: {grade}")

#Exercise 2
cities = [
    ["Sydney", "Melbourne", "Brisbane"],
    ["Karachi", "Lahore", "Islamabad"],
    ["London", "Manchester", "Birmingham"]
]

for row in cities:
    for item in row:
         print(item)

#Exercise 3
import pandas as pd
data = {
    "product": ["Laptop", "Phone", "Tablet", "Watch", "Earbuds"],
    "price": [1500, 800, 600, 300, 150],
    "rating": [4.5, 4.2, 3.8, 4.7, 3.5]
}
df = pd.DataFrame(data)
filtered_df = df[(df["price"] >400) & (df["rating"] > 4.0)]
sorted_df = filtered_df.sort_values("price", ascending=False)
print(sorted_df)