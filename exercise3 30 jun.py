import pandas as pd

data = {
    "products" : ["iphone", "macbook", "ipad", "vison pro", "watch"],
    "price" : [2200, 5000, 2500, 6000, 1300]
}
df = pd.DataFrame(data)
sorted_data = df.sort_values("price", ascending=False)
print(sorted_data)