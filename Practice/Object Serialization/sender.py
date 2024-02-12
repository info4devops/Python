# sender.py is responsible to serialize an employee object to file

from emp import*
import pickle

f=open('emp2.dat','wb')
while True:
  eno=int(input('Enter Employee Number:'))
  ename=input('Enter Employee Name:')
  esal=int(input('Enter Employee Salary:'))
  eaddr=input('Enter Employee Address:')
  e=Employee(eno,ename,esal,eaddr)
  pickle.dump(e,f)
  option=input('Do You want to serialize one more Employee Object[Yes/No]:')
  if option.lower() in ['no','n']:
    break

print('All Objects are serialized Successfully')
f.close()