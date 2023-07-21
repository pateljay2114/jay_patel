# Write a Python function to check whether a number is in a given range

def checknumber(num):
    
    if num in range(1,100):
        print("The number is in range.")
    else:
        print("The number is not in range.")

num = int(input("Enter the number : "))

checknumber(num)