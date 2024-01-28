# __str__(): which used to print output in readable form
class Student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
    
  def __str__(self):
    return 'Name:{} & marks:{}'.format(self.name,self.marks)

s1=Student('Virat',99)
s2=Student('Rohit',79)
print(s1)

print(type(s1))
print(s2)