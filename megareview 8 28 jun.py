class shape:
    def area(Self):
        return 0
class square(shape):
       def __init__(self, side):
           self.side = side
       def area(self):
          return self.side * self.side
       
square = square(5)
print(square.area())
        
