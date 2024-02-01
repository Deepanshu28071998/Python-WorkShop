
l=int(input("Enter the number of elements in the list: "))
ns=[]
for i in range(l):
    n=int(input("Enter number {}:".format(i+1)))
    ns.append(n)
print(list(ns))
print(tuple(ns))
print(set(ns))


'''
# This program takes a list of numbers from the user and prints the sum of the numbers.

# Get the number of elements in the list from the user.
n = int(input("Enter the number of elements in the list: "))

# Create an empty list to store the numbers.
numbers = []

# Get the numbers from the user and add them to the list.
for i in range(n):
    number = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(number)

# Print the sum of the numbers.
print("The sum of the numbers is:", sum(numbers))
'''
