# whenever we are creating child class object,only child class construction will be execute.
#If child class has no constructor then only parent class constructor will be execute
# If we want to execute both parent and child class constructor while creating child class object then we should use super() function

# Child Class With Constructor
print(':::::::::Child Class With Constructor::::::::')
class Parent:
  def __init__(self):
    print('Parent Class: Constructor')

class Child(Parent):
  def __init__(self):
    print('Child Class: Constructor')

c=Child()
print()

# Child Class With Constructor
print(':::::::::Child Class Without Constructor::::::::')
class Parent:
  def __init__(self):
    print('Parent Class: Constructor')

class Child(Parent):
  pass

c=Child()