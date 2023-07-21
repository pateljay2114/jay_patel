""" 
Write a Python program to create a dictionary from a string.
o Note: Track the count of the letters from the string. Sample string:
'w3resource'
o Expected output: {'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


"""

sample_string = "w3resource"
dict1 = {}

for i in sample_string :
    
    dict1[i] = dict1.get(i,0)+1
    
print(dict1)