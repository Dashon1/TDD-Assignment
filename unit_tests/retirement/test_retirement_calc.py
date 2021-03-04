import unittest
from retirement_calc import retirement_calc

class testRetirementCalc(unittest.TestCase):
    #only need one test to see if it is right because the print result function
    #will handle whether or not the result is valid
    def test_with_age_0_salary100000_percent10_goal1000000(self):
        actual = retirement_calc( 100000, 10, 1000000)
        expected = 74

        #see if all went well
        self.assertEqual(actual, expected)