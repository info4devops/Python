# WAP to generate fibonacci serices using generators functions

def fibonacci_serices(n):
  a,b=0,1
  while a<=n:
    yield a
    a,b = b,a+b
    
n=int(input('Enter Max-value to generate fibonacci serice:'))
for i in fibonacci_serices(n):
  print(i,end=' ')
print()

