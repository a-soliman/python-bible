# parameteres vs argumants
def about( name, age, likes ): # parameters
	sentence = 'Meet {}, they are {} years old, and they like {}.'.format(name, age, likes)
	return sentence

print(about('Jack', 23, 'Python')) #argumanrs

print(about(age = 25, likes='JavaScript', name = 'Ahmed'))# keyword argumants

# default values parametes
def greet(name, age, likes='Python and C++'):
	sentence = 'Greetings {}, glad that you like {}.'.format(name, likes)
	return sentence

print(greet('Emmy', 26))
print(greet('Mona', 29, 'JavaScript'))