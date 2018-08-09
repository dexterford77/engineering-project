from pathlib import Path
import unittest
from utils import create_email_body, get_num_of_commissions


class TestUtils(unittest.TestCase):
  """Tests for utils.py"""


  def setUp(self):
    self.good_file = Path("examples/good_file.txt")
    self.corrupt_file = Path("examples/corrupt.txt")


  def test_get_num_of_commissions(self):

    # if given valid input, it returns an integer
    self.assertEqual(type(get_num_of_commissions(self.good_file)), type(1))

    # if given corrupt input, it raises an error
    with self.assertRaises(ValueError):
      get_num_of_commissions(self.corrupt_file)


  def test_create_email_body(self):

    # it returns a string
    self.assertEqual(type(create_email_body(self.good_file)), type("This is a string."))

    # the returned string contains the expected total amount, implying that all of the transaction lines have been summed correctly
    body = create_email_body(self.good_file)
    result = body.find("353.7")
    self.assertNotEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
