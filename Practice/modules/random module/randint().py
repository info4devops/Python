#syntax: randint(start,end)
#paramentes: (start,end) Both of them must be integer values
#Return: A random interger in range(start,end) including the end points

from random import*
a=int(input('Enter start value:'))
b=int(input('Enter End value:'))

r1=randint(a,b)
print(f'Random number between {a} and {b} is:{r1}')

# Using for loop
n=int(input('Enter range value:'))
print(f'The random {n} integers between {a} and {b} are:')
for i in range(n):
  print(randint(a,b),end=",")