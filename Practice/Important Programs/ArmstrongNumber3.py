# Python Program to Check Armstrong Number
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
# Example: 153

n = int(input("Enter Number to Check:")) # taking input from user
s = n  # assigning input value to the s variable
b = len(str(n)) # converting int to str and finding it length

sum1 = 0
while n != 0:
    r = n % 10 # Units digit
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print(f'The given number:{s}, and it is armstrong number')
else:
    print(f'The given number:{s}, and it is not an armstrong number')
