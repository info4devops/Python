# Creating bytearray:range 0-255
b=bytearray()
print('b:',b)
print('Type of b:',type(b))
print()

# Creating bytearray with some elements:using list
L=[10,20,123,222]
print('Type of L:',type(L))
b1=bytearray(L)
print('list of b1:',list(b1))
print('Type of b1:',b1)
# printing each element
for x in b1:
    print(x,end=' ')
print('\n')

# Indexing & Slicing
print('1st Elements: ',b1[0])
print('Last Element: ',b1[-1])
print('L[0:3]: ',b1[0:3])
# printing each element
for x in b1[0:3]:
    print(x,end=' ')
print('\n')
print('L[::-1]: ',b1[::-1])
# printing each element
for x in b1[::-1]:
    print(x,end=' ')
print('\n')

# Creating bytearray with some elements:using tuple
T=(10,20,123,222)
print('Type of T:',type(T))
b2=bytearray(T)
print('tuple of b2:',tuple(b2))
print('Type of b2:',b2)

# printing each element
for x in b2:
    print(x,end=' ')
print('\n')

# Replacing elements of bytes
b2[0]=121
b2[1]=131
print('After replacing,elements in b2:')
for x in b2:
    print(x,end=' ')
