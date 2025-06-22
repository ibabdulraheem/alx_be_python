import math
class Shape:
  def __init__(self):
    pass
  def area(self):
    raise NotImplementedError ("derived classes need to override this method.")

class Rectangle(Shape):
  def __init__(self,length,width):
    self.length = length
    self.width = width
    super().__init__()
  def area(self):
    self.area = self.length * self.width
    return self.area
    
class Circle(Shape):
  def __init__(self,radius):
    self.radius = radius
    super().__init__()
  def area(self):
    return(self.radius **2) * math.pi
