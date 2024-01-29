# generator functions: Genrate a sequence of objects without storing

def first_n_values (n):
  x=1
  while x<=n:
    yield x
    x=x+1

values = first_n_values(5)
for value in values:
  print(value,end=' ')