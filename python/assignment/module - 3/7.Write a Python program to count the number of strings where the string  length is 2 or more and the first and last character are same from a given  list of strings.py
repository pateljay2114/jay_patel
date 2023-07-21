# # Write a Python program to count the number of strings where the string length is 2 or more and the first and
# # last character are same from a given list of strings
string_list = []
length = int(input("Enter your string length : "))

for i in range(0,length):
    string_=input("Enter of string : ")
    string_list.append(string_)

count = 0
print(string_list)
for i in string_list:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
        
print("\nFirst and last Same character in string : ",count)        


