from random import*
start = int(input('Enter start value: '))
stop = int(input('Enter stop value: '))
if start>stop:
  small = stop
  large = start
else:
  small = start
  large = stop
print(large,small)


