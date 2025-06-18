class SimpleCalculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        """Return the addition of a and b."""
        return self.a + self.b

    def subtract(self):
        """Return the subtraction of b from a."""
        return self.a - self.b

    def multiply(self):
        """Return the multiplication of a and b."""
        return self.a * self.b

    def divide(self):
        """Return the division of a by b. Returns None if b is zero."""
        if self.b == 0:
            return None
        return self.a / self.b
    
my_calculator = SimpleCalculator()
print(my_calculator.add(10,5))