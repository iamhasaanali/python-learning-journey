#exercise 1 Describe and adding new colum
import pandas as pd
data = {
    "name" : ["Hasaan", "Ali", "Sara", "Ahmad", "Fatima"],
    "age" : [27, 22, 25, 30, 28],
    "salary" : [70000, 45000, 60000, 85000, 55000]
 }
df = pd.DataFrame(data)
print(df.describe())
df["senior"] = df["age"] > 27
print(df.groupby("senior")["salary"].mean())



#exercise 2 handle missing data
import pandas as pd
import numpy as np
data = {
    "name" : ["Hasaan", "Ali", "Sara", "Ahmad", "Fatima"],
    "age" : [27, None, 25, 30, None],
    "salary" : [70000, 45000, None, 85000, 55000]
 }
df = pd.DataFrame(data)
print(df)
print("-----")
print(df.isnull().sum())

#exercise 3.0 FIX the missing data approach 1 fills none with mean values
import pandas as pd
import numpy as np
data = {
    "name" : ["Hasaan", "Ali", "Sara", "Ahmad", "Fatima"],
    "age" : [27, None, 25, 30, None],
    "salary" : [70000, 45000, None, 85000, 55000]
 }
df = pd.DataFrame(data)
df["age"] = df["age"].fillna(df["age"].mean())
df
print(df)

#exercise 3.1 FIX the missing data approach 2 remove rows of none
import pandas as pd
import numpy as np
data = {
    "name" : ["Hasaan", "Ali", "Sara", "Ahmad", "Fatima"],
    "age" : [27, None, 25, 30, None],
    "salary" : [70000, 45000, None, 85000, 55000]
 }
df = pd.DataFrame(data)
df_Clean = df.dropna()
print(df_Clean)