num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))

if num1 == num2 or num2 == num3 or num3 == num1:
    print("0")
else:
    print("sum of three number : ",num1+num2+num3)    