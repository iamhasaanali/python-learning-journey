class person:
    total_persons = 0

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        person.total_persons += 1
    def introduce(self):
        print("Hi, iam", self.name, "I am", self.age, "I live in", self.city)
    def birthday(self):
        self.age = self.age + 1
        print(self.name, "is now", self.age, "yeras old")

my_person1 = person("Hasaan", 27, "Sydney")
my_person2 = person("Sara", 25, "London")

my_person1.introduce()
my_person1.birthday()
print("----")
my_person2.introduce()
my_person2.birthday()

print(person.total_persons)
