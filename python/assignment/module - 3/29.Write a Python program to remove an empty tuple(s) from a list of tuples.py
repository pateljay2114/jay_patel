# Write a Python program to remove an empty tuple(s) from a list of tuples.


l1 = [(1,2),("jay",),(),(3,4),(),(10)]
l2 = []

for i in l1:
    if len(i) == 0 :
        l1.remove(i)

print(l1)



