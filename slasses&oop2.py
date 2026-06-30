class person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, I'm", self.name)

class studnet(person):
    def __init__(self, name, age, school):
        super().__init__(name,age)
        self.school = school

    def study(self):
        print(self.name, "is studying at", self.school)

s1 = studnet("Hasaan", 27, "Self-Taught Academy")
s2 = studnet("Ali", 22, "Tech University")
s1.introduce()
s1.study()
print("---")
s2.introduce()
s2.study()

