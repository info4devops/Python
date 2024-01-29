# generator functions: Genrate a sequence of objects without storing

def CountDown(n):
  print('Start Count Down')
  while n>0:
    yield n
    n=n-1
n=int(input('Enter max-Value from where countdown shpuld starts:'))
values = CountDown(n)
for value in values:
  print(value)
print('Count Down Ends')