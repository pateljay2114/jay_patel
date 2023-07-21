# Write a Python program to returns sum of all divisors of a number


num1= int(input("Enter Number : "))
sum = 0


if num1 > 0 :
    for i in range(1,num1+1):
        if num1 % i == 0:
            sum += i
    print("Sum Of All Divisor : ", sum)
    
else:
    print("Sum Of All Divisor : ", sum)