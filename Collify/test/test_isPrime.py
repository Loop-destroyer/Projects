# import required libraries 
from unittest import TestCase 
from isPrime import isPrime 

# define a class 
class CalculatorTest(TestCase): 
	
	# test case for checking non prime nums 
	def test_nonprime(self): 
		self.assertEqual(isPrime(12),False) 
	
	# test case to check prime nums 
	def test_prime(self): 
		self.assertEqual(isPrime(19),True) 

	# test case to check invalid input 
	def test_invalid(self): 
		self.assertEqual(isPrime(-1),False)
