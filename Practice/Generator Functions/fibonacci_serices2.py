# WAP to generate fibonacci serices using generators functions

def fibonacci_serices(n):
  a,b=0,1
  while True:
    yield a
    a,b = b,a+b

count=1
n=int(input('How many fibonacci serices you required:'))
for i in fibonacci_serices(n):
  if count>n:
    break
  print(i,end=' ')
  count=count+1
