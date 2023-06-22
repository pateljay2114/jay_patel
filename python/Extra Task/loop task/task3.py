# taks - accept how many name user wants to add

add_Name = int(input("Enter you want to add name : "))
names = []

for i in range(1,add_Name+1):
    name = input("Enter the name : ")
    names.append(name)

print(names)    