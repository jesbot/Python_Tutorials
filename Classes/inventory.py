class Inventory(object):

	def __init__(self, items):
		self.items = items

	def add(self, item):
		if self.items.haskey(item):
			self.items[item] += 1
		else:
			self.items[item] = 1

	def remove(self, item):
		if self.items.haskey(item):
			if self.items[item] < 1:
				print "Can go negative. Sorry"
			else:
				self.items[item] -= 1

	def check(self, item):
		if self.items.haskey(item):
			return True 
		else:
			return False

	def print_inventory(self):
		for item in self.items:
				print item, "-", slef.items[item]
