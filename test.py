class Test:
    n=1212
    def __init__(self):
        self.a=10
        self.b=20
        self.a=999
        Test.n=2121

    def m1(self):
        Test.n=2121
        print(self.a)
        print(self.b)
t=Test()
t2=Test()
t.m1()
t.a = 111
print(t.a)
print(t2.a)
print(Test.n)

    