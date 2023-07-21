# Write a Python script to concatenate following dictionaries to create a new one.

dict1 = {'name': 'jay','python': 85, 'marks': 60}
dict2 = {'php': 'avinash','java': 190, 'cpp': 40}
dict3 = {'city': 'lunawada','nord.js': 78, '.net': 80}

concate_dic = {}

for i in (dict1,dict2,dict3):
    concate_dic.update(i)

print(concate_dic)