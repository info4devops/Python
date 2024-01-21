a=10 # global
def f1():
  a=777 # local
  print(f'f1_local:{2}')
  print(f'Global from f1 is:{globals()["a"]}')

f1()
print(a)
