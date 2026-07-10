#exercise 1
import pandas as pd
data = {
    "country": ["Australia", "Pakistan", "England", "UAE"],
    "population": [26000000, 230000000, 56000000, 10000000],
    "gdp": [1700, 350, 3100, 500]
}
df = pd.DataFrame(data)
print(df.describe())
print("-----")
df["wealthy"] = df["gdp"] > 1000
print(df)
print("----------------------------")


#exercise 2
import pandas as pd
data = {
    "country": ["Australia", "Pakistan", "England", "UAE"],
    "population": [26000000, 230000000, 56000000, 10000000],
    "gdp": [1700, 350, 3100, 500]
}
df = pd.DataFrame(data)
df["wealthy"] = df["gdp"] > 1000
print(df[df["wealthy"]])
print("-----")
print(df.sort_values("population", ascending=False))
print("-----")
print(df.groupby("wealthy")["gdp"].mean())
print("----------------------------")

#exercise 3
import pandas as pd
data = {
    "product": ["Laptop", "Phone", "Tablet", "Watch", "Earbuds"],
    "category": ["Electronics", "Electronics", "Electronics", "Wearables", "Wearables"],
    "price": [1500, 800, 600, 300, 150]
}
df = pd.DataFrame(data)
print(df.shape)
print("-----")
print(df.head(3))
print("-----")
print(df["category"].value_counts())
print("-----")
print(df[df["price"] > 500])
print("-----")
print(df.sort_values("price", ascending=True).head(1))
print("----------------------------")

#exercise 4

players = ["Babar", "Kohli", "Smith", "Root"]
scores = [85, 92, 78, 88]
combined = zip(players, scores)
result = dict(combined)
for players,scores in result.items():
    print(f"{players} scored {scores} runs")

top_scorers = [player for player, score in result.items() if score > 85]
print(top_scorers)
print("----------------------------")

#exercise 5
import pandas as pd

data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "city": ["Sydney", "Karachi", "Sydney", "London", "Karachi"],
    "score": [85, 92, 78, 95, 60],
    "age": [27, None, 25, 30, None]
}

df = pd.DataFrame(data)
print(df)
print("-----")
print(df.isnull().sum())
print("-----")
df["age"] = df["age"].fillna(df["age"].mean())
print(df)
print("-----")
print(df[df["score"] > 80])
print("-----")
print(df.groupby("city")["score"].mean())
print("-----")
print(df.sort_values("score", ascending=False).head(1))