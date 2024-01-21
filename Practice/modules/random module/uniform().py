# uniform(intx,inty): It returns random float values between 2 given numbers(Not inclusive)

from random import*
a=int(input('Enter start value:'))
b=int(input('Enter End value:'))

r1=uniform(a,b)
print(f'Random number between {a} and {b} is:{r1}')

# Using for loop
n=int(input('Enter range value:'))
print(f'The random {n} integers between {a} and {b} are:')
for i in range(n):
  print(uniform(a,b),end=",")