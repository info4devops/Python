try:
  print('stmt-1')
  print('stmt-2')
  print('stmt-3')
  try:
    print('stmt-4')
    print('stmt-5')
    print('stmt-6')
  except ValueError:
    print('stmt-7')
  finally: 
    print('stmt-8')
    print('stmt-9')
    
except ZeroDivisionError:
  print('stmt-10')
  
finally:
  print(10/0)
print('stmt-12')