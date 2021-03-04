import unittest
from print_result2 import print_result2

class testPrintResult2(unittest.TestCase):
    #testing results when age is 100 since this should be invalid the result is 30 but irrelevant
    def test_with_age_100(self):
        actual = print_result2(100, 30)
        expected = "You'll be dead before you reach the desired savings goal."

        #see if everything goes well
        self.assertEqual(actual, expected)

    #testing with an age of 0 since that is the lower boundary and result of 99
    #which should be valid, 99 is also the upper boundary on the age
    def test_with_age_0_result99(self):
        actual = print_result2(0, 99)
        expected = 99

        #if all went well we should see 99 which is the result
        self.assertEqual(actual, expected)

    