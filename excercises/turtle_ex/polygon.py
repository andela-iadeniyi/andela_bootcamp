import math
class Polygon(object):
	"""docstring for Polygon"""
	radius = "radius"
	sides = "sides"
	def __init__(self, radius, sides):
		super(Polygon, self).__init__()
		self.radius = radius
		self.sides = sides

	def find_lenth(self):
		angle = float(360 / self.sides)
		otherangle = float((180 - angle) / 2)
		radangle = float(angle * (math.pi / 180))
		radangle2 = float(otherangle * (math.pi/180))
		angles = math.sin(radangle) / math.sin(radangle2)
		lenth = self.radius * angles
		return lenth

n = Polygon(100, 5)
print n.find_lenth()
		