class Calculator:
  calculation_type = "Arithmetic Operations"
  
  @staticmethod
  def add (a ,b):
    return a + b
  
  @classmethod
  def multiplication(cls ,a,b):
    print(f"Calculation type: {cls.calculation_type}")
    return a * b
  
print(Calculator.multiply(2,3))
print(Calculator.add(4,5))



  