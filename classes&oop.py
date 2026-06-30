class dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(self.name, "Say woof")
        print("Breed is", self.breed)

    def birthday(self):
        self.age = self.age + 1
        print(self.name, "is now", self.age, "years old")


my_dog1 = dog("Bella", "Poodle", 3)
my_dog2 = dog("Rex", "Lebrador", 5)
my_dog1.bark()
my_dog1.birthday()
my_dog1.birthday()
print("---")
my_dog2.bark()
my_dog2.birthday()
my_dog2.birthday()