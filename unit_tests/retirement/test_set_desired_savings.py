import unittest

from set_desired_savings import set_desired_savings

class testSetDesiredSavings(unittest.TestCase):
    def test_set_desired_savings_0(self):
        #testing with 0 which is valid if the person does not want to save anything
        actual = set_desired_savings(0)
        expected = True

        self.assertEqual(actual, expected)

    #testing with 100 billion which is the upper limit
    def test_set_desired_savings_100_bill(self):
        actual = set_desired_savings(100000000000)
        expected = True

        self.assertEqual(actual, expected)

    #testing with greater than 100,000,000,000 which is invalid. Don't be greedy
    def test_set_desired_savings_100_plus_bill(self):
        with self.assertRaises(ValueError) as exception_context:
            set_desired_savings(100000000001)
            self.assertEqual(str(exception_context.exception), "Please don't attempt to save this amount. This is way too much for any one person.")

    #testing with a negative number which should be invalid unless they want to go into debt
    def test_set_desired_savings_neg1(self):
        with self.assertRaises(ValueError) as exception_context:
            set_desired_savings(-1)
            self.assertEqual(str(exception_context.exception), "Desired savings can not be negative unless you want to go into debt.")