# Write a Python script to check if a given key already exists in a dictionary.

dict1 = {1 : 'python', 2 : 'java', 3 : 'noed.js',4 : 'php'}
check_key = int(input("Enter the key you check : "))

if check_key in dict1:
    print("Key is already exit in a dictionary.")
else:
    print("Key is not exit in a dictionary.")