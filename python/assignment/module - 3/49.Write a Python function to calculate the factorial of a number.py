# Write a Python function to calculate the factorial of a number (a non-negative integer)


import math

def factorial(num):
    if num < 0:
        print("Your number is negative.")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:    
        print("Your number is positive.")
        num1 = math.factorial(num)
        return print("Factorial Number : ",num1)

    
num = int(input("Enter Number You Wnat to Find Factorial : "))
factorial(num)

""" 
def factorial():
    factorial = 1

    if num > 0:
        for i in range ( 1, num + 1):
            factorial = factorial * i
        print(factorial)
    elif num < 0:
        print("factorial does not for negative numbers")
    else:
        print("The factorial of 0 is 1")


num = int(input("Enter Number You Wnat to Find Factorial : "))

factorial()
"""