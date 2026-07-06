#exercise 1

school = {
    "class_a": {"students": 30, "teacher": "Mr. Smith"},
    "class_b": {"students": 25, "teacher": "Ms. Jones"},
    "class_c": {"students": 28, "teacher": "Mr. Brown"}
}

for n in school:
    print("class name:", n)
    print("number of students:", school[n]["students"])
    print("teacher:", school[n]["teacher"])
    print("------------------------------")
   
#exercise 2
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def circumference(self):
        return 2 * 3.14 * self.radius
    def is_large(self):
        return True if self.radius > 10 else False

c1 = circle(5)
c2 = circle(15)
print("Area of circle 1:", c1.area())
print("Circumference of circle 1:", c1.circumference())
print("Is circle 1 large?", c1.is_large())
print("Area of circle 2:", c2.area())
print("Circumference of circle 2:", c2.circumference())
print("Is circle 2 large?", c2.is_large())

#exercise 3 in study_log.py

