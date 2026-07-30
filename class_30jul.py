players = ["Babar", "Kohli", "Smith", "Root", "Williamson"]
print(players[:3])    # first 3 items
print(players[2:])    # from position 2 to end
print(players[-2:])   # last 2 items
print(players[::2])   # every other item
print(players[::-1])  # reverse the whole list!
print("--------------------------------")
import pandas as pd

df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara"],
    "salary": [70000, 45000, 65000],
    "years": [6, 3, 7]
})

def calculate_bonus(row):
    if row["years"] > 5 and row["salary"] > 60000:
        return row["salary"] * 0.15
    else:
        return row["salary"] * 0.05

df["bonus"] = df.apply(calculate_bonus, axis=1)
print(df)
print("")

import pandas as pd
df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed"],
    "math": [85, 42, 91, 68],
    "english": [78, 65, 88, 72]
})
def overall_grade(row):
    if row["math"] > 80 and row["english"] > 80:
        return f"Distinction"
    elif row["math"] > 60 and row["english"] > 60:
        return f"Pass"
    else:
        return f"Fail"

df["result"] = df.apply(overall_grade, axis=1)
print(df)