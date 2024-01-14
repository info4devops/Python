# Identity Operator: compare reference of argument
a=int(input('Enter a:'))
b=int(input('Enter b:'))
print(f'Id of a:{id(a)} \nId of b:{id(b)}')
print(f'The result of (a is b) : {a is b}')
print(f'The result of (a is not b) : {a is not b}')
print()

# Membership Operator: checks if an argument is present in sequence or not
string=input('Enter any string:')
sub_string=input('Enter substring to find:')
print(f'"{sub_string}" is present in "{string}"?: {sub_string in string}')
print(f'"{sub_string}" is not present in "{string}"?: {sub_string not in string}')
