# setter method: used to set the values to the instance variable
# getter method: used to get the values to the instance variable

class Student:
  # Setter methods
  def setName(self,name):
    self.name=name
  def setMarks(self,marks):
    self.marks=marks
  # getter methods
  def getName(self):
    return self.name
  def getmarks(self):
    return self.marks

n=int(input('Enter number of student:'))
for i in range(n):
  s=Student()
  name=input('Enter name:')
  s.setName(name)
  marks=int(input('Enter marks:'))
  s.setMarks(marks)
  
  print('Hi,',s.getName())
  print('Your Marks are:',s.getmarks())
  print()
