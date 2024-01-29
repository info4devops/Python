# If try with multiple except blocks available, Then default except block should be last other wise we will get Syntax Error.

try:
  x=int(input('x='))
  y=int(input('y='))

  print(x/y)
  

except ZeroDivisionError as msg :
  print('Exception Name:{}'.format(msg.__class__.__name__))
  print('Exception Description:{}'.format(msg))
  print('Exception Type:{}'.format(type(msg).__name__))

# Default Except Block
except:
  print('Default Excetion Message')
  