# Write a Python script to sort (ascending and descending) a dictionary by value.

dict1 = {'python': 10, 'java': 2, 'nord.js': 8, 'tops': 5   }
print(dict1)

ascending = dict(sorted(dict1.items(), key=lambda x: x[1]))
descending = dict(sorted(dict1.items(), key=lambda x: x[1], reverse=True))
print("\nDictionary in ascending :",ascending)
print("Dictionary in descending :",descending)

