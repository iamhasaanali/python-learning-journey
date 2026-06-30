class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class manager(employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    def info(self):
        print(self.name, "manages team of", self.team_size, "people, earning", "$",self.salary)

m1 = manager("Hasaan", 100000, 3)

m1.info()
