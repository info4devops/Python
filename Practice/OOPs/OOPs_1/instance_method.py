# Instance method

class Student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
  def display(self):
    print('Hi,',self.name)
    print('Your Marks are:',self.marks)
  def grade(self):
    if self.marks>=60:
      print('You got 1st rank')
    elif self.makrs>=50:
      print('You got 2nd rank')
    elif self.makrs>=35:
      print('You got 3rd rank')
    else:
      print('You are failed')
n=int(input('Enter number of student:'))
for i in range(n):
  name=input('Enter name:')
  marks=int(input('Enter marks:'))
  s=Student(name,marks)
  s.display()
  s.grade()
  print()

    