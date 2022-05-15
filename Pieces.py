

class King:

	def __init__(self, pos, colour):
		self.pos = pos
		self.colour = colour
		self.label = 'K'
		self.checks = []

	def __str__(self):
		return 'K'

class Queen:

	def __init__(self, pos, colour):
		self.pos = pos
		self.colour = colour
		self.label = 'Q'
		self.checks = []

	def __str__(self):
		return 'Q'

class Bishop:

	def __init__(self, pos, colour):
		self.pos = pos
		self.colour = colour
		self.label = 'B'
		self.checks = []

	def __str__(self):
		return 'B'

class Knight:

	def __init__(self, pos, colour):
		self.pos = pos
		self.colour = colour
		self.label = 'N'
		self.checks = []

	def __str__(self):
		return 'N'

class Rook:

	def __init__(self, pos, colour):
		self.pos = pos
		self.colour = colour
		self.label = 'R'
		self.checks = []

	def __str__(self):
		return 'R'

class Pawn:

	def __init__(self, pos, colour):
		self.pos = pos
		self.colour = colour
		self.label = 'P'
		self.checks = []

	def __str__(self):
		return 'P'










