import pandas as pd
data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "city": ["Sydney", "Karachi", "Singapore", "London", "Sydney"],
    "score": [85, 72, 91, 68, 78]
}
df = pd.DataFrame(data)
high = df[(df["score"] > 80) & (df["city"].str.startswith("S"))]
sydney = df[(df["score"] > 80) | (df["city"] == "Sydney")]
print(high)
print("-------")
print(sydney)
print("-------")
print(df[df["city"].str.startswith("S")])
print("-------")
print(df[df["city"].str.contains("on")])
print("-------")
print(df[df["name"].str.endswith("a")])
print("-------")
print(df[df["city"].str.contains("sydney")])
print("-------")
print(df[df["city"].str.contains("sydney", case=False)])
print("-------")
print(df[df["name"].str.len() > 4])
print("-------")
print(df["city"].str.replace("Sydney", "Melbourne"))
print("\n-------------------------")

#exercise 2
import pandas as pd
data = {
    "product": ["iPhone 17", "Samsung S25", "MacBook Pro", "iPad Mini", "Surface Pro"],
    "brand": ["Apple", "Samsung", "Apple", "Apple", "Microsoft"],
    "price": [2200, 1800, 3999, 800, 1500],
    "category": ["Phone", "Phone", "Laptop", "Tablet", "Laptop"]
}
df = pd.DataFrame(data)
print(df[df["brand"] == "Apple"])
print("-------")
print(df[df["product"].str.contains("Pro")])
print("-------")
print(df[(df["price"] > 1500) & (df["category"] == "Laptop")])
print("-------")
print(df[(df["brand"].str.startswith("S")) | (df["price"] < 1000)])
print("-------")
df["expensive"] = df["price"] > 2000
df["brand"] = (df["brand"].str.replace("apple", "🍎 Apple", case=False))
print(df)