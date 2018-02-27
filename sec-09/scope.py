a = 110

def f1():
	global a
	a = 90
	print(a)

def f2():
	a = 50
	print(a)

f1()
f2()
print(a)

myList = [ 2,4,5 ]

print(myList)

def f3():
	myList[0] = 11
	print(myList)

def f4():
	myList = 44
	print(myList)

f3()
f4()
print(myList)