# Write a Python program to find the second smallest number in a list.


l1 = [] 
n = int(input("Enter the number of elements: "))

for i in range(1, n+1): 
    elem = int(input("Enter the elements: ")) 
    l1.append(elem) 
    
l1.sort() 
print("The sorted list: ", l1) 
print("The second smallest value of this list: ",l1[1])