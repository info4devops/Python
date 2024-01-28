# Finding MRO

class A:
  pass
class B(A):
  pass
class C(A):
  pass
class D(B,C):
  pass

print(':::::::MRO(A):::::::::')
print(A.mro())

print('\n:::::::MRO(B):::::::::')
print(B.mro())

print('\n:::::::MRO(C):::::::::')
print(C.mro())

print('\n:::::::MRO(D):::::::::')
print(D.mro())