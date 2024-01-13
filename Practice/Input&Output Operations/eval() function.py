# About eval() function: automatically convert into corresponding data type as per input value
a=eval(input('Enter any value:'))
print(f'Type of a:{type(a)}')

# It is used to solve expression
a=input('Enter any expression:')
print(f'Type of a: {type(a)}')
result=eval(a)
print(f'The result:{result}')
print(f'Type of result: {type(result)}')
