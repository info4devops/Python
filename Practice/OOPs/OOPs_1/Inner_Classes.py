# Program about inner classes

class Outer:
  def __init__(self):
    print('Outer class object creation')
  class Inner:
    def __init__(self):
      print('Inner class object creation')
    def m1(self):
      print('Inner class method')

o=Outer()  #Outer class object creation
i=o.Inner() #Inner class object creation
# Accessing inner class method-case:1
print('::::::::::Case:1-Accessing inner class method::::::::')
i.m1()
print('::::::::::Case:2-Accessing inner class method::::::::')
i=Outer().Inner()
i.m1()
print('::::::::::Case:3-Accessing inner class method::::::::')
i=Outer().Inner().m1()
