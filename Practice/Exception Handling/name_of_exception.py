# Program to print name of the exception rised
# Every exception is a child class to BaseException class

try:
  print(10/0)
except BaseException as msg:
  print('The Name of Exception:{} '.format(msg.__class__.__name__))
  print('The Type of Exception:{} '.format(type(msg).__name__))

  