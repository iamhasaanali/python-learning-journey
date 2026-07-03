class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def describe(self):
        print("This is a ", self.brand, self.model)

class electric_vehicle(vehicle):
    def describe(self):
        print("This is an electric ", self.brand, self.model)

vehicle1 = vehicle("Toyota", "Corolla")
electric_vehicle1 = electric_vehicle("Tesla", "Model S")

vehicle1.describe()
electric_vehicle1.describe()