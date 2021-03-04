import unittest
from set_salary import set_salary

class testSetSalary(unittest.TestCase):
    #testing with salary being 0 which should fail
    def test_salary_0(self):
        with self.assertRaises(ValueError) as exception_context:
            set_salary(0)
            self.assertEqual(str(exception_context.exception), "You have to make some money in order to save anything")

    #testing with the upper limit
    def test_salary_1bill(self):
        actual = set_salary(1000000000)
        expected = True

        #see if we get true
        self.assertEqual(actual,expected)

    #test with a number just over the limit
    def test_salary_1bill_plus_1(self):
        with self.assertRaises(ValueError) as exception_context:
            set_salary(1000000001)
            self.assertEqual(str(exception_context.exception), "If you make this much money, you don't need to worry about saving.")