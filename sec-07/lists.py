our_list = [4, 14, 55, 60, 17]

# Type
print(type(our_list))

# table list
our_table = [ [1,2,3] , [4,5,6] , [7,8,9] ]
print(our_table[0][1])


# ADDING TO LIST
a = [2,4,6,7]
print(a)


# adding through append
a.append('Ahmed')

# adding through +
a = a + ['ab', 'a']

# adding through list()
a = a + list(str(123))

# adding list to a list
a = a + [ [7,7,7] ]
a.append([5,5,5])
print(a)


# instering to a list
b = [5, 12, 72, 55, 89, 1]
b.insert(2, 100)
b.insert(3, ['a','b','c'])

print(b)