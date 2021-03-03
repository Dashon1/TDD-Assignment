import unittest
from set_weight import set_weight

class testSetWeight(unittest.TestCase):
    def test_set_weight_0(self):
        #test to see if value error is raised when given the number 0 as input
        with self.assertRaises(ValueError) as exception_context:
            set_weight(0)
            self.assertEqual(str(exception_context.exception), "You can't weigh nothing.")

    def test_set_weight_neg1(self):
        #test to see if value error is raised when the number -1 is given as input
        with self.assertRaises(ValueError) as exception_context:
            set_weight(-1)
            self.assertEqual(str(exception_context.exception), "I'm not a physicist, but I think it's impossible for a human to weigh less than nothing.")
    
    def test_set_weight_1(self):
        #testing with 1 since that should be a valid weight and is at the lower boundary
        actual = set_weight(1)
        expected = True
        
        #should return True if all goes well
        self.assertEqual(actual, expected)

    def test_set_weight_599(self):
        #testing with weight being 599 pounds since it is valid and at the upper boundary
        actual = set_weight(599)
        expected = True
        
        #should return True if all goes well
        self.assertEqual(actual, expected)

    def test_set_weight_601(self):
        #testing with weight equal to 601 pounds since it is right above the upper boundary and should be invalid
        with self.assertRaises(ValueError) as exception_context:
            set_weight(601)
            self.assertEqual(str(exception_context.exception), "You can not weigh more than 600 pounds. If you weigh anywhere near this much you have bigger problems.")