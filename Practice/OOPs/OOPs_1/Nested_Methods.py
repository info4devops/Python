#Nested Methods: Method inside a method
# Required: With in the method,if any functionality repeatedly required.

class Test:
  def m1(self):
    def calc(a,b):
      print('The Sum:',a+b)
      print('The Difference:',a-b)
      print('The Product:',a*b,'\n')
    calc(10,20)
    calc(111,222)

t=Test()
t.m1()