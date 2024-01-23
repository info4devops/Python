# we are not required to provide value for self variable, PVM itself will provide values for self

class Test:
  def __init__(self):
    print('Constructor')
  
  def m1(self,x):
    print('m1 method')

t=Test() # Constructor
t.m1(10) # m1 method
t.m1() # TypeError: Test.m1() missing 1 required positional argument: 'x'
