#Write a Python program to find the repeated items of a tuple.


t = ("jay",44,True,46,"avinash","jay",44,"jay")

repeat_list = []

for i in t:
    if t.count(i) > 1 and i not in repeat_list:
        repeat_list.append(i)
        
print(repeat_list)        






