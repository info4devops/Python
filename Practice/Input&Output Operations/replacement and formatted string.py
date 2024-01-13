# print with replacement operators
a='Virat'
b=76
print('Hello,{} scored {} centuries in ODIs for india'.format(a,b))
print()
print('Hello,{0} scored {1} centuries in ODIs for india'.format(a,b))
print()
print('Hello,{p} scored {q} centuries in ODIs for india'.format(p=a,q=b))


#print with formatted string
a=10
print('a value:%i'%a)
x=20
y=30
print('x=%d,y=%d'%(x,y))

# formatted string
price=50.342567892
print('Price value={}'.format(price))
print('Price value=%.1f'%price)
print('Price value=%.2f'%price)
print('Price value=%.3f'%price)
print('Price value=%.4f'%price)
print('Price value=%.5f'%price)


