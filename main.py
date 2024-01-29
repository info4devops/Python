try:
  print('stmt-1')
  print('stmt-2')
  print('stmt-3')
except ValueError:
  print(10/0)
finally:
  print('stmt-5')
  print('stmt-6')