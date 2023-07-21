# # Write a Python script to print a dictionary where the keys are numbers between 1 and 15.


# dic1 = {1:"name1",2:"name2",3:"name3",4:"name4",5:"name5",6:"name6",7:"name7",8:"name8",9:"name9",10:"name10",11:"name11",12:"name12",13:"name13",14:"name14",15:"name15",16:"name16",17:"name17"}

# for k,v in dic1.items():
#     if k > 0 and k <= 15:
#         print(k,v)
        
dict1 = {}

for i in range(1,16):
    dict1[i] = None

print(dict1)        
        