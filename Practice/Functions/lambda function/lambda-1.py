# anonymous function: function without name
# lambda syntax: lambda argument_list:expression

#lambda function to find square of a given number

n=int(input('Enter any value:'))
s= lambda n:n*n # lambda function
print(f'The square of {n} is:{s(n)}')

#lambda function to find sum of a two number
a=int(input('Enter a value:'))
b=int(input('Enter b value:'))

s= lambda a,b:a+b # lambda function
print(f'The sum of {a} and {b} is:{s(a,b)}')
