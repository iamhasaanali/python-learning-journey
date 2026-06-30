class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
    def accelration(self, amount):
        self.speed = self.speed + amount
        print(self.brand, self.model, "is now going", self.speed, "km/h")
    def brake(self, amount):
        self.speed = self.speed - amount
        print(self.brand, self.model, "is now going", self.speed, "km/h")
class car(vehicle):
    def __init__(self, brand, model, door):
        super().__init__(brand, model)
        self.door = door
    def honk(self):
        print(self.brand, self.model,"has",self.door, "doors and it says beep beep")


c1 = car("Honda", "Civic", 4)
c2 = car("Audi", "Q7", 5)

c1.accelration(55)
c1.brake(23)
c1.honk()
print("-----")
c2.accelration(110)
c2.brake(33)
c2.honk()
