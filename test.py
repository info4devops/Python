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
