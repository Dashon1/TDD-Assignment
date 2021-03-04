import unittest
from set_percent_saved import set_percent_saved

class testPercentSaved(unittest.TestCase):
    #testing with 0 which is valid because it is possible to save nothing
    def test_percent_saved_0(self):
        actual = set_percent_saved(0)
        expected = True

        self.assertEqual(actual, expected)

    #testing with 100 which is also valid because it is technically possible to be able to save everything
    def test_percent_saved_100(self):
        actual = set_percent_saved(100)
        expected = True

        self.assertEqual(actual, expected)

    #testing with -1 which is invalid, I thing you would own money at this point
    def test_percent_saved_neg1(self):
        with self.assertRaises(ValueError) as exception_context:
            set_percent_saved(-1)
            self.assertEqual(str(exception_context.exception), "Percent saved can not be less than 0. I think you owe money at this point.")

    #testing with > 100 which is invalid. I'm guessing you would be stealing if you are doing this
    def test_percent_saved_101(self):
        with self.assertRaises(ValueError) as exception_context:
            set_percent_saved(101)
            self.assertEqual(str(exception_context.exception), "Percent saved can not be greater than 100. You are probably stealing if you can save more than the amount of money you recieve from your check.")