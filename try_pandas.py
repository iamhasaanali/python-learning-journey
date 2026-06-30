import pandas as pd

data = {
    "name" : ["Hasaan", "Ali", "Sara"],
    "age" : [27, 22, 25],
    "city": ["Sydney", "Karachi", "London"]

}
df = pd.DataFrame(data)
adults = df[df["age"] >= 25]
print(adults)
