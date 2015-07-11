import unittest, funwithfibo

class checkfibo(unittest.TestCase):
	def testZero(self):
		self.assertEqual(funwithfibo.fibo(0), 0, msg="the input is 0")

	def testZeroless(self):
		self.assertEqual(funwithfibo.fibo(-1), 0, msg="the input is less than 0")
	
	def testNotDigit(self):
		self.assertEqual(funwithfibo.fibo("adee1@"), 0, msg="Not a valid digit")

	def testfiboSumZero(self):
		self.assertEqual(funwithfibo.fibo_sum(0, None), 0, msg="the input is less than 0")

	def testfiboSumZeroless(self):
		self.assertEqual(funwithfibo.fibo_sum(-1, None), 0, msg="the fibo_sum input is less than 0")
	
	def testfiboSumNotDigit(self):
		self.assertEqual(funwithfibo.fibo_sum("adee1@", None), 0, msg="Not a valid digit")

	def testNotEven(self):
		self.assertTrue(funwithfibo.fibo_sum(4, "odd"), msg="fibo sum second value not odd")

	def testNotOdd(self):
		self.assertTrue(funwithfibo.fibo_sum(4, "even"), msg="fibo sum second value not even")

	def testNotEvenorOdd(self):
		self.assertTrue(funwithfibo.fibo_sum(4, None), msg="fibo sum second value not even or odd")

if __name__ == "__main__":
	unittest.main()