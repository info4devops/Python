# To find out the relationship between 2 int values

x = int(input('Enter x: '))
y = int(input('Enter y: '))

print(f'Relation between x and y is: ')
if x==y:
  print('Both x and y are equal')
else:
  if x<y:
    print(f'x:{x} is less than y:{y}')
  else:
    print(f'x:{x} is greater than y:{y}')


    
  