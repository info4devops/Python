# Try with multiple except blocks

try:
  x=int(input('x='))
  y=int(input('y='))

  print(x/y)
  
except ZeroDivisionError:
  print('Zero Division Error raised')
except ValueError:
  print('Value Error raised')
  
   