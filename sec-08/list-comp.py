even_numbers = [x for x in range(0,101) if x % 2 == 2]

print(even_numbers)

words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
answer = [ [j.upper(), j.lower(), len(j) ] for j in words ]
print(answer)