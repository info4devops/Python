# Operator Over Loading

class Employee:
  def __init__(self,name,day_salary):
    self.name=name
    self.day_salary=day_salary
  # magic method
  def __mul__(self,other):
    total_salary = self.day_salary*other.days
    return total_salary

class TimeSheet:
  def __init__(self,name,days):
    self.name=name
    self.days=days

e=Employee('Virat',500)
t=TimeSheet('Virat',25)

print('Per day salary:{}'.format(e.day_salary))
print('No.of Days:{}'.format(t.days))
print('The Total Salary:{}'.format(e*t))

#print('The Total Salary:{}'.format(t*e)) #TypeError: unsupported operand type(s) for *: 'TimeSheet' and 'Employee'
