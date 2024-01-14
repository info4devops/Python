#Ternary Operator: if Operator is applicable for three arguments
a=int(input('Enter a:'))
b=int(input('Enter b:'))
result= a if a>b else b
print(f'The Large number is {result}')

# Nesting of Ternary Operators : ternary operator in ternary operator
x=int(input('Enter x:'))
y=int(input('Enter y:'))
z=int(input('Enter z:'))

# find max number
Max_number= x if x>y and x>z else y if y>z else z
print(f'The largest number is {Max_number}')

# find min number
Min_number= x if x<y and x<z else y if y<z else z
print(f'The Smallest number is {Min_number}')


