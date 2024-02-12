# NOte: dump(),dumps(),load() and loads() will work only on dict objects

# Seraialization  & De-Seraialization of custom class objects
import json
# Creating Employee class
class Employee:
  def __init__(self,eno,ename):
    self.eno=eno
    self.ename=ename
    
# Displya class for printing 
  def display(self):
    print('Number:',self.eno)
    print('Name:',self.ename)

# Creating Employee Object
e=Employee(111,'virat')
print('Type of e:',type(e)) # <class '__main__.Employee'>
print()

# converting employee main class object to dict

emp_dict=e.__dict__
print('Type of emp_dict:',type(emp_dict))
print()

#serilization
with open('emp3.json','w') as f:
  json.dump(emp_dict,f,indent=4)

#De-serilization
with open('emp3.json','r') as f:
  d=json.load(f)

New_Employee = Employee(d['eno'],d['ename'])
New_Employee.display()


