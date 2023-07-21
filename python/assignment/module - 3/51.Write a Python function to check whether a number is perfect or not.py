# Write a Python function to check whether a number is perfect or not.
     
def is_perfect_number(number):
    if number <= 0:
        return False

    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    return divisor_sum == number

# Example usage:
num = int(input("Enter the Number : "))

if is_perfect_number(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")    