#exercise 1
import pandas as pd

df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/students.csv")

print("shape:", df.shape)
print("Columns:", df.columns.tolist())
print("----")
print(df.head(3))
print("----")
print(df.tail(3))
print("----")
print(df.describe())

#exercise 2
import pandas as pd

df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/students.csv")

print(df.groupby("city")["grade"].mean())
print("----")
print(df["city"].value_counts())
print("----")
print(df.sort_values("grade", ascending=False).head(3))
# Only Sydney students above grade 70:
sydney = df[df["city"] == "Sydney"]
print(sydney[sydney["grade"] > 70])
print(sydney)