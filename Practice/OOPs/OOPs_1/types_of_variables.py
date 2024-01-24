# Python class has 3 type of variables

class student:
  college_name = 'IIT Bombay' # Static Variable
  def __init__(self,name):
    self.name=name # Instance variable
  
  def m1(self):
    x=5 # Local variable
    for i in range(x):
      print(i,end='')

s=student('virat')
s.m1()

