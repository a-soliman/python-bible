vowels = 0
cons = 0

for letter in "Ahmed":
	if letter.lower() in 'aeiou':
		vowels = vowels +1

	elif letter == ' ':
		pass

	else:
		cons = cons + 1

#print('{} Vows., {} cons.'.format(vowels, cons))

students = {
	"male": ["Tom", "John", "Mike", "Dan"],
	"female": ["Sarah", "Huda", "Emily"]
}

for key in students.keys():
	for name in students[key]:
		if 'a' in name:
			print(name)


for i in range(0,11):
	print(i)