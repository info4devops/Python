 # WAP to generate fake employee data for database testing
 
from random import*
alphabets = 'abcdefghijklmnopqrstuvwxyz'
digits ='0123456789'
cities=['Hyd','Blr','Pune','Delhi','Mumbai']
designations=['software engineer','senior software engineer','Team Lead','Manager','Project Manager','project Lead']

# To generate fake name
def get_fake_name():
  name=choice(alphabets).upper()
  n=randint(2,9)
  for i in range(n):
    name=name+choice(alphabets)
  return name

# To generate employee ID
def get_fake_eno():
  eno='e-'
  for i in range(4):
    eno=eno+choice(digits)
  return eno

# To get salary of employee
def get_fake_salary():
  esal=uniform(10000,50000) # print floting value include ranges
  return esal

# To get city of employee
def get_fake_city():
  city = choice(cities)
  return city

# To get designation
def get_fake_designation():
  designation = choice(designations)
  return designation

# To get fake mobile number
def get_fake_mno():
  mno=choice('6789')
  for i in range(9):
    mno=mno+choice(digits)
  return mno

# To get complete employee date
def get_fake_emp_date():
  print(f'Employee Name:{get_fake_name()}')
  print(f'Employee ID:{get_fake_eno()}')
  print(f'City:{get_fake_city()}')
  print(f'Designation:{get_fake_designation()}')
  print('Salary:{:.2f}'.format(get_fake_salary()))
  print(f'Mobile Number:{get_fake_mno()}')
  
# Calling employee date
n=int(input('Enter number of employess:'))
for i in range(n):
  get_fake_emp_date()
  print()
 