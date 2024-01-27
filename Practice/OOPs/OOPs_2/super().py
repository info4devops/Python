#If we want to execute both parent and child class constructor while creating child class object then we should use super() function

# Child Class With Constructor
print(':::::::::Without super() function::::::::')
class Parent:
  def __init__(self):
    print('Parent Class: Constructor')

class Child(Parent):
  def __init__(self):
    print('Child Class: Constructor')

c=Child()
print()

print(':::::::::With super() function::::::::')
class Parent:
  def __init__(self):
    print('Parent Class: Constructor')

class Child(Parent):
  def __init__(self):
    super().__init__() #making parent class constructor available for child class
    print('Child Class: Constructor')

c=Child()
print()
