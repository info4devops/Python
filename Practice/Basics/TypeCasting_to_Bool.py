# Type casting to bool
# zero--> False & non Zero--> True
# int to bool
a=11
n=bool(a)
print('n:',n)
print('type of n:',type(n))
print()

# float to bool
a1=22.01
n1=bool(a1)
print('n1:',n1)
print('type of n1:',type(n1))
print()

a11=0.00
n11=bool(a11)
print('n11:',n11)
print('type of n11:',type(n11))
print()

# complex to bool
a2=11+2j
n2=bool(a2)
print('n2:',n2)
print('type of n2:',type(n2))
print()

# str to bool
a3='234'
n3=bool(a3)
print('n3:',n3)
print('type of n3:',type(n3))
print()

a4='' # empty string
n4=bool(a4)
print('n4:',n4)
print('type of n4:',type(n4))


