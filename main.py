try:
  x=int(input('x='))
  y=int(input('y='))

  print(x/y)
  

except ZeroDivisionError:
  print('Zero Division Error')
except ValueError:
  print('Value Error')
  
   