class BinarySearch(list):
	def __init__(self, a, b):
		data = range(0, a, b)
		super(BinarySearch, self).__init__(data)

	def ad(self, n):
		last = len(self) -1
		first = 0
		count = 0
		pos = {}
		while first <= last:
			#print count
			count += 1
			m = (first + last) // 2
			if self[m] == n:
				return {"index":m, "count":count}
			else:
				if self[m] > n:
					last = m - 1
				else:
					first = m + 1
			#count += 1
		#return pos

a = [6,7,10,30,100,150,200,210]

n = BinarySearch(20, 2)
print n.ad(10)
#print ad(a, 6)`