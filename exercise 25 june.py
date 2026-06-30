class animal:
    total_animals = 0

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        animal.total_animals += 1
    def make_sound(self):
        print(self.name, "says", self.sound)

class cat(animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
    def scratch(self):
        print(self.name, "is scratching")

c1 = cat("Roxy", "meoww")
c2 = cat("tommy", "meoww")

c1.make_sound()
c2.make_sound()
print("Total animals created: ", animal.total_animals)
    