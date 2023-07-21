# Write a Python program to find the highest 3 values in a dictionary


dict1 = {"a": 200, 'b': 100, 'c': 50, 'd': 300, 'e': 10}
l1 = []

for i in dict1.values():
    l1.append(i)

l1.sort(reverse=True)
print(l1[:3])