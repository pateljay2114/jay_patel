# Write a Python program to generate and print a list of first and last 5 
#elements where the values are square of numbers between 1 and 30.


# squares = 5**3
# print(squares)

# Generate a list of squares of numbers between 1 and 30
#squares = [i**2 for i in range(1, 31)]

list = []
for i in range(1,31):
    list.append(i)
print(list)    
    
# Print the first 5 elements
print("First 5 elements:")
for num in list[:5]:
    print(num**2)

# Print the last 5 elements
print("Last 5 elements:")
for num in list[-5:]:
    print(num**2)
