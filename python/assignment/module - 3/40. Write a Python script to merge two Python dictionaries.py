#  Write a Python script to merge two Python dictionaries.

dict1 = {1 : 'python', 2 : 'java', 3 : 'php',}
dict2 = { 4 : 'nord.js', 5 : 'Tops', 6 : 'avinash'}

dict3 = {}
# method 1
dict3.update(dict1)
dict3.update(dict2)
print(dict3)

# method 2
for i in (dict1,dict2):
    dict3.update(i)
print(dict3)