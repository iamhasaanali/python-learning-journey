import numpy as np
salaries = np.array([70000, 45000, 65000, 80000, 55000, 75000, 90000])
print(np.sum(salaries))
print(np.mean(salaries))
print(np.max(salaries))
print(np.min(salaries))
print(np.std(salaries))
print(salaries*1.1)
print(salaries[salaries>65000])
print(np.sort(salaries)[::-1])
print("-------------------------------")
#exercise 2
import numpy as np
scores = np.array([
    [85, 92, 78, 88],
    [90, 65, 88, 72],
    [72, 95, 83, 91],
    [68, 78, 95, 85]
])
print(scores.shape)
print(np.mean(scores, axis = 1))
print(np.mean(scores, axis = 0))
print(np.max(scores))
print(scores[1])
print(scores[:2])
print("-------------------------------")
#exercise 3
import pandas as pd
import numpy as np
data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "salary": [70000, 45000, 65000, 80000, 55000],
    "score": [85, 72, 91, 68, 78]
}
df = pd.DataFrame(data)
print(np.mean(df["salary"]))
print(np.max(df["score"]))
df["salary_scaled"] = df["salary"] / np.max(df["salary"])
print(df)
print(df.loc[df["salary"].idxmax()])
print("-------------------------------")

#exercise 4
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Product:
    def __init__(self,name,price,launch_date):
        self.name = name
        self.price = price
        self.launch_date = launch_date
    def age_months(self):
        today = datetime.now()
        diff = relativedelta(today,self.launch_date)
        return diff.years * 12 + diff.months
    def is_discounted(self):
        if self.age_months() > 18:
            return True
        else:
            return False
    def final_price(self):
        if self.is_discounted() == True:
            return self.price * 0.85
        else:
            return self.price

p1 = Product("Laptop", 2500, datetime(2023, 1, 1))
p2 = Product("Phone", 1200, datetime(2024, 6, 1))
p3 = Product("Tablet", 800, datetime(2022, 3, 15))
products = [p1,p2,p3]
data = []
for p in products:
    data.append({
        "name": p.name,
        "price": p.price,
        "age_months": p.age_months(),
        "is_discounted": p.is_discounted(),
        "final_price": p.final_price()
    })

df = pd.DataFrame(data)
print(df)