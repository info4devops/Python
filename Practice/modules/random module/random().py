# syntax: random.random()
# parameters: This method does not accept any parameters
# Return: This method returns a random floating number between 0 and 1

# Implementing the random function from random module
print(':::::Case-1:::::::::')
from random import random
print(random()) 

# Just importing random module
print('\n:::::Case-2:::::::::')
import random
print(random.random())

# random with range()
print('\n:::::Case-3:::::::::')
from random import*
for i in range(5):
  print(random())
  
