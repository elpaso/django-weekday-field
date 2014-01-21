import unittest

from fields import validate_bitwise_notation

class TestBitwiseValidation(unittest.TestCase):
  def test_zero(self):
    self.assertFalse(validate_bitwise_notation(0))

  def test_single_bit(self):
    self.assertTrue(validate_bitwise_notation(8))

  def test_multiple_bits(self):
    self.assertTrue(validate_bitwise_notation(8+16))

  def test_all_bits(self):
    self.assertTrue(validate_bitwise_notation(2**7 - 1))

  def test_invalid_number(self):
    self.assertFalse(validate_bitwise_notation(2**7))
