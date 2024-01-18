# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
values = input('Enter some comma-separated number: ') # like 2,3,4,5
list = values.split(',') # splitting str to list
print(f'List:{list}')
# converting list to tuple
tuple = tuple(list)
print(f'Tuple:{tuple}')
