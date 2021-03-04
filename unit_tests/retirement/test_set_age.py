import unittest
from set_age import set_age

class testSetAge(unittest.TestCase):
    #testing with 0 which should be valid. Assuming you were just born and your parents have already started a savings account for you.
    def test_age_0(self):
        actual = set_age(0)
        expected = True

        self.assertEqual(actual, expected)

    #testing with negative 1 should receive a value error
    def test_age_neg1(self):
        with self.assertRaises(ValueError) as exception_context:
            set_age(-1)
            self.assertEqual(str(exception_context.exception), "You have to be alive in order to save money.")

    #testing with 100 because assuming death at 100
    def test_age_100(self):
        with self.assertRaises(ValueError) as exception_context:
            set_age(100)
            self.assertEqual(str(exception_context.exception), "You have to be alive in order to save money.")
