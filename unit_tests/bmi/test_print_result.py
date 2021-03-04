import unittest
from print_result import print_result

class testPrintResult(unittest.TestCase):
    #didn't need as many test with the print function
    def test_with_string(self):
        feed = "Something"

        with self.assertRaises(TypeError) as exception_context:
            print_result(feed)
            self.assertEqual(str(exception_context.exception), "Only tuples are accepted as a valid type to print")
    
    def test_with_tuple(self):
        feed = ("33", "Super")

        #it should print this phrase inserting the two results, but for the sake of testing it needs to return this as a string.
        expected = "Your bmi is " + feed[0] + " that puts you in the " + feed[1] + " category."
        actual = print_result(feed)

        self.assertEqual(actual, expected)

