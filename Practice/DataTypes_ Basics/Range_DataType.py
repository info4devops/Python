# range(begin,end,increment/decrement)
# Range with one argument
r=range(5)
print('r:',r)
print('type of r:',r)
# printing each element from range
for x in r:
    print(x, end=' ')
print('\n') # to add space or new line

# Range with two argument
r1=range(1,10)
print('r1:',r1)
for x in r1:
    print(x, end=' ')
print('\n')

# Range with two argument
r2=range(0,50,5) #increment
print('r2:',r2)
for x in r2:
    print(x,end=' ')
print('\n')

r3=range(70,0,-7) # decrement
print('r3:',r3)
for x in r3:
    print(x,end=' ')
print('\n')

# Indexing & slicing
print('1st Elements: ',r3[0])
print('Last Element: ',r3[-1])
print('r3[0:3]: ',r3[0:3])
# printing each element
for x in r3[0:3]:
    print(x,end=' ')
print('\n')

print('r3[::-1]: ',r3[::-1])
# printing each element
for x in r3[::-1]:
    print(x,end=' ')
print('\n')