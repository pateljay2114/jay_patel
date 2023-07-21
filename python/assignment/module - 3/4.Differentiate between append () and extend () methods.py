# Differentiate between append () and extend () methods?

""""
1)append() : to stor data in existing list

2)extend(): to add more then 1 value in list 

"""
l1 = ["C", "C++","JAVA"]

for i in range(1,4):
    name = input("Enter your subject : ")
    l1.append(name)


print(l1)

l1.extend(["react","node","javascript"])
print(l1)