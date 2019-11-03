from string import ascii_lowercase as al

class Player():
	def __init__(self, sign):
		self.sign = sign

	def won(self):
		print(f'Player "{self.sign}" has won.')
		return True

class Board():
	"It's a board. Start a game with Board(board_size: int).game()"
	def __init__(self, size):
		self.size = size
		self.board = {str(i+1)+c: '#' for c in al[:self.size]*self.size for i in list(range(self.size))*self.size}


	def __str__(self):
		out = '   ' + ' '. join([str(i+1) for i in range(self.size)])
		for k, v in self.board.items():
			if '1' in k: out += f'\n {k[1]} '
			out += v + ' ' 
		return out


	def game(self):
		x, y = Player('X'), Player('O')
		print(self)
		while True:
			print('Player 1:')
			if self.move(x):
				return
			print(self)
			if '#' not in self.board.values():
				print('It\'s a tie!')
				return
			
			print('Player 2:')
			if self.move(y):
				return
			print(self)
			if '#' not in self.board.values():
				print('It\'s a tie!')
				return
		

	def move(self, player):
		while True:
			k = input('Enter field:\n').lower()
			if self.board[k] == '#':
				self.board[k] = player.sign
				if self.check(player):
					print(self)
					return True
				break
			else:
				print('Field is occupied!')


	def check(self, player):
		# Horizontal
		for c in al[:self.size]*self.size:
			x = []
			for i in range(self.size):
				x.append(self.board[str(i+1)+c])
			if len(set(x)) == 1 and player.sign in x:
				return player.won()
		# Vertical
		for i in list(range(self.size))*self.size:
			x = []
			for c in al[:self.size]:
				x.append(self.board[str(i+1)+c])
			if len(set(x)) == 1 and player.sign in x:
				return player.won()
		# Diagonal
		x = [self.board[str(i+1)+k] for i, k in enumerate(al[:self.size])]
		if len(set(x)) == 1 and player.sign in x:
			return player.won()
		x = [self.board[str(self.size-i)+k] for i, k in enumerate(al[:self.size])]
		if len(set(x)) == 1 and player.sign in x:
			return player.won()


print('\nEnter fields in format: nc, where n is integer and', 
	'\nc is character, corresponding to position on board.',
	'\nExample: "1a" is first row, first column.\n', end='')
Board(3).game()