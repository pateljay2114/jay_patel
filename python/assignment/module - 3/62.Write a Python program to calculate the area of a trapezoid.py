# Write a Python program to calculate the area of a trapezoid

t_base = float(input("Enter Top Base Of Trapezoid : "))
b_base = float(input("Enter Bottom Base Of Trapezoid : "))
height = float(input("Enter Height Of Trapezoid : "))

t_area = ( (t_base + b_base) / 2 ) * height

print("Area of Trapezoid : ", t_area)