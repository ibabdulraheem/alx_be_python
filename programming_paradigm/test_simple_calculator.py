import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator (unittest.TestCase):
  def test_addition(self):
    result = SimpleCalculator.add(10,13)
    self.assertEqual(result,23)

  def test_sub(self):
    result = SimpleCalculator.subtract(10,5)
    self.assertEqual(result,5)

  def test_mult(self):
    result = SimpleCalculator.multiply(10,5)
    self.assertEqual(result,50)

  def test_div(self):
    result = SimpleCalculator.divide(10,5)
    self.assertEqual(result,2)
    





if __name__=="__main__":
  unittest.main()