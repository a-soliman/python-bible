# PACKING
print('abc')
print(*'abc')

print('='*20)

print(1,2,3)
print([1,2,3])
print(*[1,2,3])

print('='*20)

# UNPACking 
def add( *numbers ):
	total = 0

	for number in numbers:
		total = total + number

	return total

print(add(1,2,3,4,5,6,7,8,9))

print('='*20)

# UNPACKING KEYWORD ARGS
def about( name, age, likes):
	sentence = 'Meet {}, he is {} Y.O, and he likes {}.'.format(name, age, likes)
	return sentence

print(about('John', 21, 'Python'))

dictionary = {"name": "Ahmed", "age": 30, "likes": "JS and Python"}

print('=' * 10)

print(about(**dictionary))