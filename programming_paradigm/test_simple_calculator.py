import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator (unittest.TestCase):
  my_test_cal = SimpleCalculator()
  def test_addition(self):
    result = self.my_test_cal.add(10,13)
    self.my_test_cal.assertEqual(self.my_test_cal,result,23)

  def test_sub(self):
    result = self.my_test_cal.subtract(10,5)
    self.my_test_cal.assertEqual(self.my_test_cal,result,5)

  def test_mult(self):
    result = self.my_test_cal.multiply(10,5)
    self.my_test_cal.assertEqual(result,50)

  def test_div(self):
    result = self.my_test_cal.divide(10,5)
    self.my_test_cal.assertEqual(result,2)
    





if __name__=="__main__":
  unittest.main()