#Program to perform pickling and unpickling of an employee object

import pickle
# Creating Employee Class
class Employee:
  def __init__(self,eno,ename,esal,eaddr):
    self.eno=eno
    self.ename=ename
    self.esal=esal
    self.eaddr=eaddr

# Creating display class to print employee details
  def display(self):
    print('Employee Number:',self.eno)
    print('Employee Name:',self.ename)
    print('Employee Salary:',self.esal)
    print('Employee Address:',self.eaddr)

# Creating object for employee class
e=Employee(101,'Virat',15000,'HYD')

#File Creation using with for binary-write purpose

with open('emp.dat','wb') as f:
  pickle.dump(e,f) # Serialization(pickling)
  print('Ojbect Serialization completed')

#File Creation using with for binary-write purpose

with open('emp.dat','rb') as f:
  emp=pickle.load(f) # De-Serialization(Unpickling)
  print('Ojbect De-Serialization completed')
  print()
  
  # Displaying Employee Information
  print('Printing Employee Information')
  emp.display()

  