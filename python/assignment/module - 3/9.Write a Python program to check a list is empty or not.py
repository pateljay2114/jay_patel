# Write a Python program to check a list is empty or not.

list1 = []
length = int(input("Enter your string length : "))

for i in range(0,length):
    string_=input("Enter of string : ")
    list1.append(string_)

print(len(list1))
if len(list1) == 0 :
    print("List is empty")
else:
    print("List is not empty")    