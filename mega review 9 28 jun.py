import pandas as pd

data = {
    "name" : ["Hasaan", "Ali", "Sara", "Sharjeel"],
    "salary" : [100000, 150000, 178000, 52500]
}

df = pd.DataFrame(data)
sorted_df = df.sort_values("salary", ascending=False)
print(sorted_df)