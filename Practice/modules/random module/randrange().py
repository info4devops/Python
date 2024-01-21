# randrange([begin],end,step) ==> Returns a random number from range

from random import*
start = int(input('Enter start value: '))
stop = int(input('Enter stop value: '))
if start>stop:
  small = stop
  large = start
else:
  small = start
  large = stop

# Using for loop
n= int(input('How many number you want to generate:'))
skip = int(input('Enter step value: '))
for i in range(n):
  if skip <0:
    r1 = randrange(large,small,skip)
    print(f'Random numbers between {large} and {small} by skipping {skip} is:{r1}')
  else:
    r1 = randrange(small,large,skip)
    print(f'Random numbers between {small} and {large} by skipping {skip} is:{r1}')

    



    
