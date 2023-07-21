# Write a Python program to print all unique values in a dictionary.


d1 = {'a': 33, 'b': 77, 'c':55, 'e': 77, 'f': 55, 'c':88 }
l1 = []
for i in d1.values():
    l1.append(i)

s1 = set(l1)
print(s1)

