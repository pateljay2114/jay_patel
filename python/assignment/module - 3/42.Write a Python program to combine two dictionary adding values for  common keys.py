""" 
Write a Python program to combine two dictionary adding values for common keys.

o d1 = {'a': 100, 'b': 200, 'c':300}
o d2 = {'a': 300, 'b': 200, 'd':400}

"""

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

combine_dic = {}

for i in d2.keys():
    if i in d1:
        combine_dic[i] = d1[i]+d2[i]
    else:
        combine_dic[i] = d2[i]

for i in d1.keys():
    if i not in d2:
        combine_dic[i] = d1[i]

print(combine_dic)