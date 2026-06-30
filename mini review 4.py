import pandas as pd

data = {
    "name" : ["iphon 17", "iphone air", "iphone 17 pro", "iphone 17 pro max"],
    "price" : [1700, 1850, 2000, 2200]
}
df= pd.DataFrame(data)
premium_products = df[df["price"] > 1850]
print(premium_products)
