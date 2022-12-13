import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):

  def setUp(self):
    self.calculator = Calculator()

  def test_add(self):
    self.assertEqual(self.calculator.sum(5,10), 15)

  def test_subtract(self):
    self.assertEqual(self.calculator.raz(26,13), 13)

  def test_multiply(self):
    self.assertEqual(self.calculator.proizv(4,8), 32)

  def test_divide(self):
   self.assertEqual(self.calculator.delenie(36,3), 14)

if __name__ == "main":
  unittest.main()