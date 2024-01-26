# program to check how many number of objects created for a particular class

class Test:
  count=0 #static variable
  def __init__(self):
    Test.count=Test.count+1
  @classmethod
  def noOfObjects(cls):
    print('The number of objects created for Test class:',cls.count)

t1=Test()
t2=Test()
Test.noOfObjects()
t3=Test()
t4=Test()
Test.noOfObjects()