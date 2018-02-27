import random



class Pound:

	def __init__( self, rare=False ):

		if rare == True:
			self.value = 1.25
		else: 
			self.value = 1.00

		self.color = "gold"
		self.num_edges = 1
		self.diameter = 22.5
		self.thickness = 3.15
		self.heads = True

	def __del__( self):
		print('Coin Spent!')
		return 

	def rust( self ):
		self.color = "greenish"
		return

	def clean( self ):
		self.color = "gold"
		return

	def turn_around( self ):
		if self.heads == True:
			self.heads = False
		else: 
			self.heads = True
		return

	def flip( self ):
		options = [ True, False ]
		choice = random.choice(options)
		self.heads = choice
		return


coin1 = Pound()
coin1.rust()
print(coin1.color)
coin1.clean()
print(coin1.color)
print(coin1.heads)
coin1.flip()
print(coin1.heads)
coin1.flip()
print(coin1.heads)
coin1.flip()
print(coin1.heads)

del coin1
