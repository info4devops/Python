# choice(): it wont return a random number
# It will return a random object from the given list or tuple

from random import*
l=['10','20','30','40']
for i in range(2):
  print(f'Random object from list is:{choice(l)}')
  