import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator (unittest.TestCase):
  my_test_cal = SimpleCalculator()
  def test_addition(self):
    self.assertEqual(self.my_test_cal.add(2,3),5)

  def test_sub(self):
    self.assertEqual(self.my_test_cal.subtract(10,5),5)

  def test_mult(self):
    self.assertEqual(self.my_test_cal.multiply(4,4),16)

  def test_div(self):
    self.assertEqual(self.my_test_cal.divide(6,3),2)
    





if __name__=="__main__":
  unittest.main()