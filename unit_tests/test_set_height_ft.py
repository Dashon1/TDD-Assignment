import unittest
from set_height_ft import set_height_ft

class testSetHeightFt(unittest.TestCase):
    def test_set_height_Ft_0(self):
        #test to see if value error is raised when given the number 0 as input
        with self.assertRaises(ValueError) as exception_context:
            set_height_ft(0)
            self.assertEqual(str(exception_context.exception), "You can not be 0 feet tall.")

    def test_set_height_Ft_neg1(self):
        #test to see if value error is raised when the number -1 is given as input
        with self.assertRaises(ValueError) as exception_context:
            set_height_ft(-1)
            self.assertEqual(str(exception_context.exception), "You can not be negative feet tall.")
    
    def test_set_height_Ft_5(self):
        #testing with number of feet set to 5
        actual = set_height_ft(5)
        expected = True
        
        #should return True if all goes well
        self.assertEqual(actual, expected)

    def test_set_height_Ft_8(self):
        #test to see if value error is raised when the number -1 is given as input
        with self.assertRaises(ValueError) as exception_context:
            set_height_ft(8)
            self.assertEqual(str(exception_context.exception), "Highly doubt you are 8 feet tall or above.")
