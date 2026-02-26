"""
Dante Vanderpool 
Lab 9 Unit testing
Feb 26 2026
"""
import unittest
from calculations import *

#Examople 1: simple unit testingh
#unit
def addtwonumbers(a,b):
    return a+b

#unit test
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(1,2),3)
        #test that when pass 1 and 2, the return of nthe function is 3

    #Example 2: unit testting calculation.py file
    #unit test for subtraction function
    def test_subtraction(self):
        self.assertEqual(subtracttwonumbers(6,4), 2)
        self.assertEqual(subtracttwonumbers(4,6), -2)
        self.assertEqual(subtracttwonumbers(5), 5)
        self.assertEqual(subtracttwonumbers(), 0)

    #unit test for multiplication function
    def test_multiplication(self):
        self.assertEqual(multiplythreenumbers(1,2,3,), 6)
        self.assertEqual(multiplythreenumbers(1,-2,3,), -6)
        self.assertEqual(multiplythreenumbers(1,-2,-3,), 6)
        self.assertEqual(multiplythreenumbers(-1,-2,-3,), -6)
         
    #unit test for division function
    def test_division(self):
        self.assertEqual(dividetwoumbers(6,3), 2)
        self.assertAlmostEqual(dividetwoumbers(10,3), 3.3333, places=4)

    #unit testing for division by zero
    def test_divisionbyzero(self):
        #assertion none (not returning) or some known return value 
        self.assertIsNone(dividetwonumbers(10,0))   

    #unit test for value error
        self.assertIsNone(dividetwonumbers(10,"a"))
        self.assertIsNone(dividetwonumbers("Peter", 2))

    #unit test for other possible errors by mocking
    def test_unexpected_exception(self):
        #inspect and exception to occur
        with self.assertRaises(Exception):
            #passing no values to function
            dividetwonumbers()



if __name__ == "__main__":
    unittest.main()


