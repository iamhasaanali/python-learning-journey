import pandas as pd
data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar"],
    "city": ["Sydney", "Karachi", "Sydney", "London", "Karachi", "London"],
    "score": [85, 72, 91, 68, 78, 95],
    "age": [27, 22, 25, 30, 28, 26]
}
df = pd.DataFrame(data)
df["passed"] = df["score"] >= 75
result= df.groupby("city")["score"].agg(["mean", "max", "min"]).reset_index()
sorted = result.sort_values("mean", ascending=False)
print(sorted)
print("------")
df["city_avg"] = df.groupby("city")["score"].transform("mean")
print(df)
print("------")
df["above_avg"] = df["city_avg"] < df["score"]
print(df)
print("\n----------------------------")

#exercise 2
class student:
    def __init__(self,name,city,score):
        self.name = name
        self.city = city
        self.score = score
    def grade(self):
        if self.score >= 90:
            return "A" 
        elif self.score >= 75:
            return "B"
        elif self.score >= 50:
            return "C"
        else:
            return "F"
    def display(self):
        print(f"Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Score: {self.score}")
        print(f"Grade: {self.grade()}")
        print("------------")

s1 = student("Hasaan","sydney",95)
s2 = student("Ali","Islamabad",85)
s3= student("Ahmad","Sydney",45)
s4= student("Sharjeel","Lahore", 73)
students = [s1,s2,s3,s4]
for s in students:
    s.display()
