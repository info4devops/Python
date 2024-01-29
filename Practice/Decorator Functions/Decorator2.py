# Decorator Chaining

def decor1(func):
  def inner1():
    print('Decor-1 Execution')
  return inner1

def decor2(func):
  def inner2():
    print('Decor-2 Execution')
  return inner2  

@ decor1
@ decor2

def f1():
  print('Original Function')

f1()