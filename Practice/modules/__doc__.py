# priting Doc string of a function


def f1():
  # Doc string
  """Demonstrate about DocStrings and does
  Nothing else"""
  
  return None

#Function calling
print(f1.__doc__)


# Getting doc string of math module
print(':::math module Doc String:::::\n')
import math
print(math.__doc__)

# getting the path of the current module
print('::::::::Getting Path of the module:::::::')
import os
print('Absolute Path:',os.path.abspath(__file__))
print('File name',__file__)

