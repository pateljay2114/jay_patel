# Write a Python program to check whether an element exists within a tuple.

t = (1,12,3,14,5,16,7,18,9,10)

elements =int(input("Enter number of 1 to 20 and check elelment in tuple : "))

if elements in t:
    print("the element {elements} exists in the tuple. " )
else:
    print("the element {elements} does not exists in tuple.")