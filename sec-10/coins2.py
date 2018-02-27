import random

class Coin:
	def __init__( self, clean=True, heads=True, **kwargs ):

		for key,value in kwargs.items():
			setattr(self, key, value)

			self.is_clean = clean
			self.heads = heads

		if self.is_clean:
			self.color = self.clean_color
		
		else:
			self.color = self.rusty_color

	def rust( self ):
		self.is_clean = False
		self.color = self.rusty_color
		return

	def clean( self ):
		self.is_clean = True
		self.color = self.clean_color
		return

	def flip( self ):
		options = [True, False]
		choice = random.choice(options)
		self.heads = choice
		return

	def turn_around( self ):
		if self.heads == True:
			self.heads = False
		else:
			self.heads = True

		return

class Cent(Coin):
	def __init__(self):
		data = {
			"value": 0.01,
			"clean_color": "bronze",
			"rusty_color": "brownish"
		}

		super().__init__(**data)


class Nickel(Coin):
	def __init__( self ):
		data = {
			"value": 0.05,
			"clean_color": "silver",
			"rusty_color": "darkish-silver"
		}

		super().__init__(**data)


class Dime(Coin):
	def __init__( self ):
		data = {
			"value": 0.10,
			"clean_color": "silver",
		}

		super().__init__(**data)

	def rust ( self ):
		self.color = self.clean_color
		return

	def clean ( self ):
		self.color = self.clean_color

class Qurter(Coin):
	def __init__(self):
		data = {
			"value": 0.05,
			"clean_color": "silver",
			"rusty_color": "darkish-silver"
		}

class Dollar(Coin):
	def __init__( self ):
		data = {
			"value": 1.00,
			"clean_color": "gold",
			"rusty_color": "greenish"
		}

		super().__init__(**data)



coin1 = Dollar()
coin1.rust()
print(coin1.heads)
coin1.turn_around()
print(coin1.heads)
