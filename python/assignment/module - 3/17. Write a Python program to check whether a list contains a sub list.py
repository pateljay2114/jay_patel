# Write a Python program to check whether a list contains a sub list.

 
# initializing list
l1 = [5, 6, 3, 8, 2, 1, 7, 1]
 
print("The original list : " + str(l1))
 
sublist = [8, 2, 9]
print("the sub list : ",sublist) 

# Check for Sublist in List
num=0
result=False
for i in sublist:
    if i in l1:
        num+=1
if(num==len(sublist)):
    result=True

print("Is sublist present in list ? : " + str(result))
print(num)






