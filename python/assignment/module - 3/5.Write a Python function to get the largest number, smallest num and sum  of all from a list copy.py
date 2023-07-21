# Write a Python function to get the largest number, smallest num and sum of all from a list

l1 = [10,15,20,30]

def list(l1):
    # if len(l1) == 0:
    #     return None

    largest = l1[0]
    smallest = l1[0]
    sum = 0

    for i in l1:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
        sum += i

    return largest, smallest, sum



largest, smallest, sum = list(l1)

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of all numbers:", sum)
