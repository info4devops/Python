# Logical Operators for non-boolean  values

#                AND Operator
# Returns x, if x value evaluates to false[zero value] else y 
x= int(input("Enter x:"))
y= int(input("Enter y:"))
print(f'Type of x:{type(x)} \n Type of y:{type(y)}')
result_and = x and y
print(f'Result of (x and y) is: {result_and}')

#                OR Operator
# Returns x, if x value evaluates to true[non-zero value] else y 
a= int(input("Enter a:"))
b= int(input("Enter b:"))
print(f'Type of a:{type(a)} \n Type of b:{type(b)}')
result_or = a or b
print(f'Result of (a and b) is: {result_or}')
