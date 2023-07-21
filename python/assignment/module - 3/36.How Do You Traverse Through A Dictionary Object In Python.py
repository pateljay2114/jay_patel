#  How Do You Traverse Through A Dictionary Object In Python?


"""
    To traverse through a dictionary object in Python, we have several options :

    1) Iterate over keys: we can use a for loop to iterate over the keys of the dictionary. By default, the loop will iterate over the keys
            my_dict = {'apple': 8, 'banana': 4, 'cherry': 10}
            for key in my_dict:
            print(key)

    2) Iterate over values: If we want to iterate over the values of the dictionary, we can use the values() method.
        e.g 
        
            my_dict = {'apple': 8, 'banana': 4, 'cherry': 10}
            for value in my_dict.values():
            print(value)

    3) Iterate over key-value pairs: If we want to iterate over both the keys and values simultaneously, we can use the items() method.

        e.g

            my_dict = {'apple': 8, 'banana': 4, 'cherry': 10}
            for key, value in my_dict.items():
            print(key, value)


"""