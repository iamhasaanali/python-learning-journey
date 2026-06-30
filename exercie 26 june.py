import pandas as pd
data = {
    "name" : ["Hasaan", "Ali", "Sara", "Sharjeel", "Ahmad"],
    "score" : [99, 55, 34, 88, 82],
    "subject" : ["Math", "Science", "Chemistry", "English", "Biology"]
}
df = pd.DataFrame(data)
high_scorers = df[df["score"] > 70]

print(df)
print("---")
print(high_scorers)
print("---")
print(df["name"])