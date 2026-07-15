#exercise 1
import pandas as pd
names = ["Babar Azam", "Virat Kohli", "Steve Smith", "Joe Root", "Kane Williamson"]
countries = ["Pakistan", "India", "Australia", "England", "New Zealand"]
averages = [58.3, 53.6, 61.8, 50.2, 54.7]
matches = [89, 104, 92, 131, 88]
centuries = [30, 46, 32, 31, 32]
if len(names)==len(countries)==len(averages)==len(matches)==len(centuries):
    combined = [
        {"name": name, "country": country, "average": average, "match": match, "century": century}
        for name,country,average,match,century in zip(names,countries,averages,matches,centuries)
    ]
    df = pd.DataFrame(combined)
    print(df)
else:
    print(f"List have different lengths! names={len(names)}, countries={len(countries)}, averages={len(averages)}, matches={len(matches)}, centuries={len(centuries)}")

df["is_experienced"] = df["match"] > 50
print(df)
filtered = df[df["average"] > 45]
print(filtered.sort_values("century",ascending=False))

df.to_csv("/Users/hasaanali/Documents/My_Learning/cricket_players.csv", index=False)

new_df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/cricket_players.csv")
print(new_df)
#exercise 2
class cricket_player:
    def __init__(self,name,country,average):
        self.name = name
        self.country = country
        self.average = average
    def is_elite(self):
        return self.average > 50
    def introduce(self):
        return f"I am {self.name} from {self.country} with an average of {self.average}"
c1 = cricket_player("Babar", "Pakistan", 58.3)
c2 = cricket_player("Virat", "India", 53.6)
c3 = cricket_player("Steve", "Australia", 61.8)
c4 = cricket_player("Joe", "England", 50.2)
print(c1.is_elite())
print(c1.introduce())
print(c2.is_elite())
print(c2.introduce())
print(c3.is_elite())
print(c3.introduce())
print(c4.is_elite())
print(c4.introduce())

#exercise 3
import pandas as pd

df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/cricket_players.csv")
print(df.groupby("country")["average"].mean())
print(df.groupby("country")["century"].sum())
