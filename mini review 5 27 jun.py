class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = student("Hasaan Ali", "A")
s2 = student("Ali", "B")
s3 = student("Sara", "C")
students = [s1, s2, s3]
data = {
    "name" : [s.name for s in students],
    "grade" : [s.grade for s in students]
}

import pandas as pd
df = pd.DataFrame(data)
print(df)
