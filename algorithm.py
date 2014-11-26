#!/usr/bin/python

print "hello"



class algorithm():
		def __init__(self):
				self.pegs = {}
				pass

		def create(self):
				for row in range(1,6):
						col = []
						for column in range(5-(row-1),5+(row)):
							if(row%2==0):
									if(column%2==0):
										col.append(column)
							else:
								if(column%2==1):
										col.append(column)
						self.pegs[row]=col
				return self.pegs
		
		def neighbors(self, peg):
				neighbors = {}
				row = peg[0]
				column = peg[1]
				for x in range(row-1,row+2):
					if x in self.pegs.keys():
							for y in range(column-1, column+2):
									if y in self.pegs[x]:
											col.append(y)
							neighbors[x] = col
				return neighbors
x = algorithm()
print x.create()

