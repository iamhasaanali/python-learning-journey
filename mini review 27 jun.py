class phone:
    def __init__(self, brand):
        self.brand = brand
        self.battery = 100
    def phone_usage(self, amount):
      self.battery = self.battery - amount
      print(self.brand, "battery is at", self.battery,"%")
    
p1 = phone("Apple")
p2 = phone("Samsing")

p1.phone_usage(23)
p2.phone_usage(33)