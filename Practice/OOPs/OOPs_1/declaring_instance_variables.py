# Instance varible declaration

#1. Inside constructor using self
#2. Inside Instance method using self
#3. Outside of the class using object reference of class

class Test:
    # Declaring: Inside constructor using self
    def __init__(self):
        self.a=10 # instance variable
        self.b=20
    # Declaring: Inside Instance method using self
    def m1(self):
        self.c = 999 # instance variable
t=Test()
print(t.__dict__)
t.m1() # Calling instance method 
print(t.__dict__)

# Declaring instance variable outside of the class using object reference of class
t.d=1111
t.e=2222
print(t.__dict__)

