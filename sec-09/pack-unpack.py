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