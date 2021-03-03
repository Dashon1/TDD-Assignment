import unittest
from bmi_calc import bmi_calc

class testBmiCalc(unittest.TestCase):
    def test_bmi_5ft6_150(self):
        #testing with a height of 5' 6" and a weight of 150 lbs

        #should return a list with the first element being the bmi and the second element being the category
        actual = bmi_calc(5, 6, 150)    
        expected = (24.8, "Normal weight")

        #should pass if all goes well
        self.assertEqual(actual, expected)

    def test_bmi_5f10_100(self):
        #testing with a height of 5' 10" and a weight of 100 lbs

        #should return a list with the first element being the bmi and the second element being the category
        actual = bmi_calc(5, 10, 100)    
        expected = (14.7, "Underweight")

        #should pass if all goes well
        self.assertEqual(actual, expected)

    def test_bmi_6ft0_190(self):
        #testing with a height of 6' 0" and a weight of 150 lbs

        #should return a list with the first element being the bmi and the second element being the category
        actual = bmi_calc(6, 0, 190)    
        expected = (26.4, "Overweight")

        #should pass if all goes well
        self.assertEqual(actual, expected)

    def test_bmi_6ft2_240(self):
        #testing with a height of 6' 2" and a weight of 240 lbs

        #should return a list with the first element being the bmi and the second element being the category
        actual = bmi_calc(6, 2, 240)    
        expected = (31.6, "Obese")

        #should pass if all goes well
        self.assertEqual(actual, expected)