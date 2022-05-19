from Pieces import *

"""
	TODAVIA TIENE MUCHOS ERRORES
"""

class Chess(King, Queen, Bishop, Knight, Pawn):

	def __init__(self):

		self.board = []
		info = []

		for i in range(8):

			for j in range(8):

				if (i == 0) and (j == 4):
					info.append(King((i, j),'White'))

				elif (i == 7) and (j == 4):
					info.append(King((i, j),'Black'))

				elif (i == 0) and (j == 3):
					info.append(Queen((i, j),'White'))

				elif (i == 7) and (j == 3):
					info.append(Queen((i, j),'Black'))

				elif (i == 0) and (j == 2 or j == 5):
					info.append(Bishop((i, j),'White'))

				elif (i == 7) and (j == 2 or j == 5):
					info.append(Bishop((i, j),'Black'))

				elif (i == 0) and (j == 1 or j == 6):
					info.append(Knight((i, j),'White'))

				elif (i == 7) and (j == 1 or j == 6):
					info.append(Knight((i, j),'Black'))

				elif (i == 0) and (j == 0 or j == 7):
					info.append(Rook((i, j),'White'))

				elif (i == 7) and (j == 0 or j == 7):
					info.append(Rook((i, j),'Black'))

				elif (i == 1):
					info.append(Pawn((i, j),'White'))

				elif (i == 6):
					info.append(Pawn((i, j),'Black'))							

				else:
					info.append('0')


			self.board.append(info)
			info = []

		self.board.reverse()

		self.black = self.board[0][4]
		self.white = self.board[7][4]

		self.game = []

		self.checksforWhite = []

		self.checksforblack = []


	def searchPiece(self, ide):

		pos = []

		for i in self.board:

			for j in i:

				if j != '0':

					if j.label == ide:

						pos.append(j, i)

		return pos


	def translation(self, x, y):

		transx = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

		transy = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

		return transx[x], transy[y]


	def readable(self):

		x = ''

		y = ''

		for i in self.board:

			for j in i:

				if j == '0':
					y += j + ' '

				else:	
					y += j.label + ' '

			x += '\n' + y

			y = ''


		return x


	def checkifthere(self, x, y):

		if self.board[x][y] != '0':

			return True

		return False


	def samecolour(self, x, y, a, b):

		if self.checkifthere(x, y) and self.checkifthere(a, b):

			if self.board[x][y].colour == self.board[a][b].colour:

				return True

		return False


	def move(self, x1, y1, x2, y2):

		self.board[x1][y1].pos = x2, y2
		self.board[x2][y2] =  self.board[x1][y1]
		self.board[x1][y1] = '0'

		if self.board[x2][y2].label == 'K':

			if self.board[x1][y1].colour == 'White':

				self.white = self.board[x2][y2]

			else:

				self.black = self.board[x2][y2]

		self.updatechecks()


		#PGN a tabla
		

	def tradeofpieces(self, x1, y1, x2, y2):

		if self.checkifthere(x1, y1) and self.checkifthere(x2, y2):

			if not self.samecolour(x1, y1, x2, y2):

				return True

		return False

	def pawnTakes(self, x, y, x1, y1):

		piece = self.board[x][y]
		piece2 = self.board[x1][y1]

		if abs(x - x1) == 1 and abs(y - y1) == 1 and piece.label == 'P' and piece2 != '0':

			if piece.colour == 'White':

				if x - x1 == -1 and abs(y - y1) == 1:

					return True

			else:

				if x - x1 == 1 and abs(y - y1) == 1:

					return True

		return False 


	def checkwithpawn(self, x, y):

		if self.board[x][y].colour == 'White':

			if x - 1 > -1 and y + 1 < 8:
				
				if self.board[x-1][y+1] == '0':

					self.board[x][y].checks.append((x-1, y+1)) 

			if x - 1 > -1 and y - 1 > -1:

				if self.board[x-1][y-1] == '0':

					self.board[x][y].checks.append((x-1, y-1))

		else:

			if x + 1 < 8 and y + 1 < 8:
				
				if self.board[x+1][y+1] == '0':

					self.board[x][y].checks.append((x+1, y+1)) 

			if x + 1 < 8 and y - 1 > -1:

				if self.board[x+1][y-1] == '0':

					self.board[x][y].checks.append((x+1, y-1))




	def collisionKing(self, x1, y1, x2, y2):

		if (abs(x1 - x2) == 1 or abs(x1-x2) == 0)  and (abs(y1 - y2) == 1 or abs(y1 - y2) == 0):

			if self.board[x2][y2] != '0':

				return True

		return False



	def collisionPawn(self, x, y, x1, y1):

		piece = self.board[x][y]
		piece2 = self.board[x1][y1]

		if piece.label == 'P' and abs(x - x1) == 1 or abs(x-x1) == 2:

			if piece2 == '0':

				return False

		return True


	def collisionRook(self, x1 ,y1, x2, y2):

		plus = 1

		if ((x1 - x2 == 0 and y1 - y2 != 0) or (x1 - x2 != 0 and y1 - y2 == 0)):

			if not self.samecolour(x1, y1, x2, y2):

				plus = 0

			if y1 - y2 == 0:

				for i in range(1, abs(x1 - x2) + plus):

					if x1 - x2 < 0:

						if self.checkifthere(x1 + i, y1):

							return True

					elif x1 - x2 > 0:

						if self.checkifthere(x1 - i, y1):

							return True

			elif x1 - x2 == 0:

				for i in range(1, abs(y1 - y2) + plus):

					if y1 - y2 < 0:

						if self.checkifthere(x1, y1 + i):

							return True

					elif y1 - y2 > 0:

						if self.checkifthere(x1, y1 - i):

							return True

		if x1 - x2 != 0 and y1 - y2 != 0:

			return True

		return False


	def checkwithrook(self, x1, y1):

		for i in range(1, 8):

			if x1 + i < 8:

				if self.board[x1 + i][y1] == '0':

					self.board[x1][y1].checks.append((x1 + i, y1))

			if x1 - i > -1:

				if self.board[x1-i][x1] == '0':

					self.board[x1][y1].checks.append((x1 - i, y1))

		for i in range(1, 8):

			if y1 + i < 8:

				if self.board[x1][y1+i] == '0':

					self.board[x1][y1].checks.append((x1, y1 + i))


			if y1 - i > -1:

				if self.board[x1][y1-i] == '0':

					self.board[x1][y1].checks.append((x1, y1 - i))


	def collisionBishop(self, x1, y1, x2, y2):

		plus = 1

		if x1 - x2 != 0 and abs(x1 - x2) == abs(y1 - y2):

			if not self.samecolour(x1, y1, x2, y2):

				plus = 0

			for i in range(1, abs(x1 - x2) + plus):

				if x1 - x2 > 0 and y1 - y2 > 0:

					if self.checkifthere(x1 - i, y1 - i):

						return True

				elif x1 - x2 < 0 and y1 - y2 < 0:

					if self.checkifthere(x1 + i, y1 + i):

						return True					

				elif x1 - x2 < 0 and y1 - y2 > 0:

					if self.checkifthere(x1 + i, y1 - i):

						return True

				elif x1 - x2 > 0 and y1 - y2 < 0:

					if self.checkifthere(x1 - i, y1 + i):

						return True

		return False


	def checkwithbishop(self, x1, y1):

		for i in range(1, 8):

			if abs(x1 - (x1 + i)) == abs(y1 - (y1 + i)):

				if x1 + i < 8 and y1 + i < 8:

					if self.board[x1+i][y1+i] == '0':

						self.board[x1][y1].checks.append((x1+i,y1+i))

				if x1 - i > -1 and y1 - i > -1:

					if self.board[x1-i][y1-i] == '0':

						self.board[x1][y1].checks.append((x1-i,y1-i))

				if x1 + i < 8 and y1 - i > -1:

					if self.board[x1+i][y1-i] == '0':

						self.board[x1][y1].checks.append((x1+i, y1-i))

				if x1 - i > -1 and y1 + i < 8:

					if self.board[x1-i][y1+i] == '0':

						self.board[x1][y1].checks.append((x1-i, y1+i))




	def movekNight(self, x1, y1, x2, y2):

		piece = self.board[x1][y1]
		piece2 = self.board[x2][y2]

		if piece.label == 'N':

			if abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
				
				return True 

			elif abs(x1 - x2) == 2 and abs(y1 - y2) == 1:

				return True

		return False


	def checkwithkNight(self, x1, y1):

		for i in range(1, 8):

				for j in range(1, 8):

					if (abs(x1 - (x1 + i)) == 2 and abs(y1 - (y1 + j)) == 1) or (abs(x1 - (x1 + i)) == 1 and abs(y1 - (y1 + j)) == 2):

						if x1 + i < 8 and y1 + j < 8:

							if self.board[x1+i][y1+j] == '0':

								self.board[x1][y1].checks.append((x1+i, y1+j))

						if x1 - i > -1 and y1 - j > -1:

							if self.board[x1-i][y1-j] == '0':

								self.board[x1][y1].checks.append((x1-i, y1-j))

						if x1 + i < 8 and y1 - j > -1:

							if self.board[x1+i][y1-j] == '0':

								self.board[x1][y1].checks.append((x1+i, y1-j))

						if x1 - i > -1 and y1 + j < 8:

							if self.board[x1-i][y1+j] == '0':

								self.board[x1][y1].checks.append((x1-i,y1+j))


	def collisionQueen(self, x1, y1, x2, y2):

		if not self.collisionRook(x1, y1, x2, y2) and not self.collisionBishop(x1, y1, x2, y2):			

			return False

		return True


	def checkwithqueen(self, x1, y1):

		self.checkwithrook(x1, y1)
		self.checkwithbishop(x1, y1)


	def moveKing(self, x, y, x1, y1):

		if not self.collisionKing(x, y, x1, y1) and self.nextmoveisKingincheck(x, y, x1, y1):

			self.move(x, y, x1, y1)


	def reglas(self, x1, y1, x2, y2):

		piece = self.board[x1][y1]
		piece2 = self.board[x2][y2]

		print(piece.checks)


		if piece.label == 'P':

			if self.pawnTakes(x1, y1, x2, y2):

				self.move(x1, y1, x2, y2)

				return True

			if not self.collisionPawn(x1, y1, x2, y2):

				v0 = 1


				if abs(x1 - x2) == 2:

					if x1 == 1 or x1 == 6:

						v0 = 2

				if piece.colour == 'White':

					if y1 == y2 and x1 - v0 == x2:

						print(piece.colour,'+++++')
						print(piece.label,'+++++')

						self.move(x1, y1, x2, y2)

						return True

				else:

					if y1 == y2 and x1 + v0 == x2:

						print(piece.colour,'+++++')
						print(piece.label,'+++++')

						self.move(x1, y1, x2, y2)

						return True


		elif piece.label == 'B':

			if not self.collisionBishop(x1, y1, x2, y2): 

				if piece2 == '0':

					print(piece.colour,'+++++')
					print(piece.label,'+++++')

					self.move(x1, y1, x2, y2)

					return True

				elif piece.colour != piece2.colour:

					print(piece.colour,'+++++', piece2.colour)
					print(piece.label,'+++++', piece2.label)					

					self.move(x1, y1, x2, y2)

					return True


		elif piece.label == 'R': 

			if not self.collisionRook(x1, y1, x2, y2):

				if self.tradeofpieces(x1, y1, x2, y2):

					print(piece.colour,'+++++', piece2.colour)
					print(piece.label,'+++++', piece2.label)

					self.move(x1, y1, x2, y2)

					return True

				elif piece2 == '0':


					print(piece.colour,'+++++')
					print(piece.label,'+++++')

					self.move(x1, y1, x2, y2)

					return True


		elif piece.label == 'N':

			if self.movekNight(x1, y1, x2, y2):

				if self.tradeofpieces(x1, y1, x2, y2):

					print(piece.colour,'+++++', piece2.colour)
					print(piece.label,'+++++', piece2.label)

					self.move(x1, y1, x2, y2)

					return True

				elif piece2 == '0':

					print(piece.colour,'+++++')
					print(piece.label,'+++++')

					self.move(x1, y1, x2, y2)

					return True


		elif piece.label == 'Q':

			if not self.collisionQueen(x1, y1, x2, y2):

				if self.tradeofpieces(x1, y1, x2, y2):

					print(piece.colour,'+++++', piece2.colour)
					print(piece.label,'+++++', piece2.label)

					self.move(x1, y1, x2, y2)

					return True

				elif piece2 == '0':

					print(piece.colour,'+++++')
					print(piece.label,'+++++')

					self.move(x1, y1, x2, y2)

					return True

		if self.check() == -1:

			nextpos = input('Check!. Move your king: ')

			xnext = nextpos[0]
			ynext = nextpos[1]

			ynext, xnext = self.translation(xnext, ynext)

			self.moveKing(self.black.pos[0], self.black.pos[1], xnext, ynext)

		if self.check() == 1:

			nextpos = input('Check!. Move your king: ')

			xnext = nextpos[0]
			ynext = nextpos[1]

			ynext, xnext = self.translation(xnext, ynext)

			self.moveKing(self.white.pos[0], self.white.pos[1], xnext, ynext)


		return False


	def updatechecks(self):

		lista = []

		for i in self.board:

			for j in i:

				if j != '0':

					if j.colour == 'White':

						if j.label == 'P':

							self.checkwithpawn(j.pos[0], j.pos[1])
							self.checksforblack.append(j.checks)

						if j.label == 'B':

							self.checkwithbishop(j.pos[0], j.pos[1])
							self.checksforblack.append(j.checks)

						if j.label == 'N':

							self.checkwithkNight(j.pos[0], j.pos[1])
							self.checksforblack.append(j.checks)

						if j.label == 'R':

							self.checkwithrook(j.pos[0], j.pos[1])
							self.checksforblack.append(j.checks)

						if j.label == 'Q':

							self.checkwithqueen(j.pos[0], j.pos[1])
							self.checksforblack.append(j.checks)
					else:

						if j.label == 'P':

							self.checkwithpawn(j.pos[0], j.pos[1])
							self.checksforWhite.append(j.checks)

						if j.label == 'B':

							self.checkwithbishop(j.pos[0], j.pos[1])
							self.checksforWhite.append(j.checks)

						if j.label == 'N':

							self.checkwithkNight(j.pos[0], j.pos[1])
							self.checksforWhite.append(j.checks)

						if j.label == 'R':

							self.checkwithrook(j.pos[0], j.pos[1])
							self.checksforWhite.append(j.checks)

						if j.label == 'Q':

							self.checkwithqueen(j.pos[0], j.pos[1])
							self.checksforWhite.append(j.checks)


	def nextmoveisKingincheck(self, x, y, x1, y1):

		if self.board[x][y].colour == 'White':

			for i in self.checksforWhite:

				for j in i:

					for a in j:

						if (x1, y1) == (a[0], a[1]):

							return True

		else:

			for i in self.checksforblack:

				for j in i:

					for a in j:

						if (x1, y1) == (a[0], a[1]):

							return True

		return False

	def check(self):

		for i in self.checksforWhite:

			for j in i:

				for a in j:

					if (self.white.pos[0], self.white.pos[1]) == (a[0], a[1]):

						return 1

		for i in self.checksforblack:

			for j in i:

				for a in j:

					if (self.black.pos[0], self.black.pos[1]) == (a[0], a[1]):

						return -1

		return 0


	def Play(self):

		self.updatechecks()

		print(self.readable())

		actpos = input('Posicion de pieza:')

		while True:

			#Chequear que lo que se escoja sea una pieza

			if actpos == 'q':

				break

			xact = actpos[0]
			yact = actpos[1]

			yact, xact = self.translation(xact, yact)

			if self.board[xact][yact] == '0':

				continue

			print('Pieza seleccionada:', self.board[xact][yact])

			nextpos = input('Siguiente posicion:')

			if nextpos == 'q':

				break

			xnext = nextpos[0]
			ynext = nextpos[1]

			ynext, xnext = self.translation(xnext, ynext)

			if self.reglas(xact, yact, xnext, ynext):

				print('\n')

				print(self.readable())

				actpos = input('Posicion de pieza:')


if __name__ == '__main__':
	a = Chess()
	a.Play()
