#WAP to generate fibonacci serice between some range

min_limit=int(input('Enter Start value:'))
max_limit=int(input('Enter End value:'))

def fibonacci_series():
  a,b=0,1
  while True:
    yield a
    a,b = b,a+b

count=0
for number in fibonacci_series():
  if number >=min_limit and number <=max_limit:
    print(number,end=',')
    count=count+1
  
  if number>max_limit:
    break

print('\nTotal fibonacci number present between {} and {} is:{}'.format(max_limit,max_limit,count))



