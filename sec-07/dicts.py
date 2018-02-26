students = {"Alice": 26, "Bob": 29, "Claire": 17, "Dan": 44}

print(students)

#lookup
print(students["Dan"])

#adding 
students["Emma"] = 22

#modifing
students["Alice"] = students["Alice"] + 2
print(students)

#deleting
del students["Bob"]
print(students)


# keys
keys = list(students.keys())

print(keys[1])


# values
values = list(students.values())
print(values)

students2 = {
	"Alice": 
		{
			"ID": "ID0001",
			"age": 26,
			"grade": "A"
		}, 
	"Bob": {
			"ID": "ID0001",
			"age": 32,
			"grade": "B"
		},
	"Claire": {
			"ID": "ID0001",
			"age": 17,
			"grade": "C"
		},
	"Dan": {
			"ID": "ID0001",
			"age": 24,
			"grade": "D"
		}
}

print(students2["Dan"]["age"])
clire_info = list([students2["Claire"]["ID"]])
print(clire_info)