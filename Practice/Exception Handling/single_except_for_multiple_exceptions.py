try:
  x=int(input('x='))
  y=int(input('y='))

  print(x/y)
  

except (ZeroDivisionError,ValueError,TypeError) as msg :
  print('Exception Name:{}'.format(msg.__class__.__name__))
  print('Exception Description:{}'.format(msg))
  print('Exception Type:{}'.format(type(msg).__name__))
  
   