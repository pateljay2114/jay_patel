#  Write a Python program to convert a list of tuples into a dictionary.

list1 = [(1,"java"),(2,"python"),(3,"php")]
print("List of tuple : ",list1,)

list2 = dict(list1)
type(list2)
print("Convert into dictionary : ",list2)