import unittest, fibo

class FiboTest(unittest.TestCase):
	def testZero(self):
		self.assertEqual(fibo.fibo(0), [0], msg="the input is 0")

	def testZeroless(self):
		self.assertEqual(fibo.fibo(-1), [0], msg="the input is less than 0")
	
	def testNotDigit(self):
		self.assertEqual(fibo.fibo("adee1@"), [0], msg="Not a valid digit")

	def testfiboSumZero(self):
		self.assertEqual(fibo.fibo_sum(0), [0], msg="the input is less than 0")

	def testfiboSumZeroless(self):
		self.assertEqual(fibo.fibo_sum(-1), [0], msg="the fibo_sum input is less than 0")
	
	def testfiboSumNotDigit(self):
		self.assertEqual(fibo.fibo_sum("adee1@"), [0], msg="Not a valid digit")

	def testfiboSumEvenZero(self):
		self.assertEqual(fibo.fibo_sum(0, i="even"), [0], msg="the input is less than 0")

	def testfiboSumEvenZeroless(self):
		self.assertEqual(fibo.fibo_sum(-1, i="even"), [0], msg="the fibo_sum input is less than 0")
	
	def testfiboSumEvenNotDigit(self):
		self.assertEqual(fibo.fibo_sum("adee1@", i="even"), [0], msg="Not a valid digit")

	def testfiboSumOddZero(self):
		self.assertEqual(fibo.fibo_sum(0, i="odd"), [0], msg="the input is less than 0")

	def testfiboSumOddZeroless(self):
		self.assertEqual(fibo.fibo_sum(-1, i="odd"), [0], msg="the fibo_sum input is less than 0")
	
	def testfiboSumOddNotDigit(self):
		self.assertEqual(fibo.fibo_sum("adee1@", i="odd"), [0], msg="Not a valid digit")

if __name__ == "__main__":
	unittest.main()