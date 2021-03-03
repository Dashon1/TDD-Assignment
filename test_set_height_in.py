import unittest
from set_height_in import set_height_in

class testSetHeightIn(unittest.TestCase):
    def test_set_height_in_0(self):
        #0 is a valid number of inches so test to see if it returns true
        actual = set_height_in(0)
        expected = True
        
        self.assertEqual(actual, expected)

    def test_set_height_in_neg1(self):
        #test to see if value error is raised when the number -1 is given as input
        with self.assertRaises(ValueError) as exception_context:
            set_height_in(-1)
            self.assertEqual(str(exception_context.exception), "You can not subtract from your height using negative inches.")
    
    def test_set_height_in_8(self):
        #testing with number of inches set to 8
        actual = set_height_in(8)
        expected = True
        
        #should return True if all goes well
        self.assertEqual(actual, expected)

    def test_set_height_in_13(self):
        #test to see if value error is raised when the number 13 is given
        with self.assertRaises(ValueError) as exception_context:
            set_height_in(13)
            self.assertEqual(str(exception_context.exception), "If the number of inches is can not be greater than 12. Just add 1 to your height in feet.")
