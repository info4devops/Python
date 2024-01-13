# Arora number: ex: 153
# sum of squares of digits in number = number
# taking input from user
n=input('Enter n:')
# converting str into int type
s=int(n)
l=[] # empty list
sum=0

# iterating each string in n
for x in n:
    # converting into int value
    digit=int(x)
    # adding int value to list
    l.append(digit)
# printing list value
print(f'list:{l}')

for x in l:
    # finding the square for each digit
    square_value=x**3
    # adding the square value to sun
    sum=sum+square_value

# Printing total sum value
print(f'The sum:{sum}')

# checking sum of squares of number is equal to n or not
if s == sum:
    print(f'{n} is Armstrong number')
else:
    print(f'{n} is not Armstrong number')


