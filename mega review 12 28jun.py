import pandas as pd
class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
p1 = product("iphone", 2200)
p2 = product("Mac", 3999)
p3 = product("Watch", 1300)
p4 = product("airpods", 400)

products = [p1, p2, p3, p4]

data = {
    "name" : [p.name for p in products],
    "price" : [p.price for p in products]

}

df = pd.DataFrame(data)
expensive = df[df["price"] > 50]
print(expensive)