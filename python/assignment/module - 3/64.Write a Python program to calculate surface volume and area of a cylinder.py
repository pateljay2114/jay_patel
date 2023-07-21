# Write a Python program to calculate surface volume and area of a cylinder

c_radius = float(input("Enter Radius of Cylinder : "))
c_height = float(input("Enter Height of Cylinder : "))


surfaceArea = 2 * 3.14 * c_radius * (c_radius + c_height) 
volumeCylinder = 2 * 3.14 * (c_radius**2) * c_height

print("Surface Area of Cylinder : ", surfaceArea)
print("Volume of Cylinder : ", volumeCylinder)