# Creating bytes:range 0-255
b=bytes()
print('b:',b)
print('Type of b:',type(b))
print()

# Creating bytes with some elements:using list
L=[10,20,123,222]
print('Type of L:',type(L))
b1=bytes(L)
print('list of b1:',list(b1)) # printing in list form
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

# Creating bytes with some elements:using tuple
T=(10,20,123,222)
print('Type of T:',type(T))
b2=bytes(T)
print('b2:',b2)
print('Type of b2:',b2)

# printing each element
for x in b2:
    print(x,end=' ')
print('\n')

