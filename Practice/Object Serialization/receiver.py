# receiver.py is responsible to deserialize employee object from file
import pickle
f=open('emp2.dat','rb')
print('De-serializing Employee Object and Printing Employee Data')
print()

while True:
  try:
    obj=pickle.load(f)
    obj.display()
    print()
  except EOFError:
    print('All Employess Completed')
    break
