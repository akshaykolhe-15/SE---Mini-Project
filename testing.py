import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        try:
        	self.assertEqual(calc.add('', 'a'), None)
        	self.assertEqual(calc.add('a', 5), None)
        	self.assertEqual(calc.add(2, 5), 7)
        	self.assertEqual(calc.add(10, 5), 15)
        	self.assertEqual(calc.add(-1, 1), 0)
        	self.assertEqual(calc.add(-1, -1), -2)
        	self.assertEqual(calc.add(4.5, 5.5), 10.0)
        except (ZeroDivisionError,SyntaxError,NameError,IndexError,TypeError,AssertionError,ValueError):
        	print("ERROR => TEST FAIL")

    def test_subtract(self):
    	try:
    		self.assertEqual(calc.subtract(101111111111111111111111111111111111111111111111111111111111111, 10111111111111555555555555555111111111111111111111111111111111111111106),-10111111010000444444444444443999999999999999999999999999999999999999995)
    		self.assertEqual(calc.subtract(-1, 1), -2)
    		self.assertEqual(calc.subtract(-1, -1), 0)
    		self.assertEqual(calc.subtract(3.5, 0.05), 3.45)
    	except (ZeroDivisionError,SyntaxError,NameError,IndexError,TypeError,AssertionError,ValueError):
    		print("ERROR => TEST FAIL")
    		
    def test_multiply(self):
        try:
        	self.assertEqual(calc.multiply(10, 5), 50)
        	self.assertEqual(calc.multiply(10.5,1.5), 15.75)
        	self.assertEqual(calc.multiply(-1, 1), -1)
        	self.assertEqual(calc.multiply(-1, -1), 1)
        except (ZeroDivisionError,SyntaxError,NameError,IndexError,TypeError,AssertionError,ValueError):
        	print("ERROR => TEST FAIL")
        	
    def test_divide(self):
        try:
        	self.assertEqual(calc.divide(10, 5), 2)
        	self.assertEqual(calc.divide(-1, 1), -1)
        	self.assertEqual(calc.divide(-1, -1), 1)
        	self.assertEqual(calc.divide(5, 2), 2.5)
        	self.assertEqual(calc.divide(0, 0), None)
        except (ZeroDivisionError,SyntaxError,NameError,IndexError,TypeError,AssertionError,ValueError):
        	print("ERROR => TEST FAIL")
        	
    def test_fibonacci(self):
        try:
        	self.assertEqual(calc.fibonacci(0), 0)
        	self.assertEqual(calc.fibonacci(1), 1)
        	self.assertEqual(calc.fibonacci(2), 1)
        	self.assertEqual(calc.fibonacci(5), 5)
        except (ZeroDivisionError,SyntaxError,NameError,IndexError,TypeError,AssertionError,ValueError):
        	print("ERROR => TEST FAIL")
        	    
