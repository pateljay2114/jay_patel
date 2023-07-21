#  Write a Python program to remove duplicates from a list.
unique_list = []

l1 = ["java","python","java"]


# s = set(l1)
# print(s)


for i in l1:
    
    if i not in unique_list:
        unique_list.append(i)
        
print(unique_list)

