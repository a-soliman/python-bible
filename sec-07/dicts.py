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