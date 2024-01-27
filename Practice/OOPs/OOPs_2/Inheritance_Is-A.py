# Inheritance: Whatever variables,method and  constructors available in parent class by default available to child class.

class Parent:
  a=888
  def __init__(self):
    print('Parent Class: Constructor')
    self.b=999
  def m1(self):
    print('Parent Class:Instance Method')
  @classmethod
  def m2(cls):
    print('Parent Class:Class Method')
  @staticmethod
  def m3():
    print('Parent Class:Static Method')

class Child(Parent):
  @staticmethod
  def m4():
    print('Child Class: Static Method')

print(':::::::Accessing Using Child class :::::')
c=Child()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
c.m4()

print('\n:::::::Accessing Using Parent class :::::')
p=Parent()
print(p.a)
print(p.b)
p.m1()
p.m2()
p.m3()
# Method m4() is available in child class but we tried to access using parent class reference
#p.m4() # AttributeError: 'Parent' object has no attribute 'm4'. Did you mean: 'm1'?
