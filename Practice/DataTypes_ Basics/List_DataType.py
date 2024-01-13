# creating list
L1=[] # Empty list
print('L1: ',L1)
print('type of L1:',type(L1))
print()

#List with some elements
L=[10,25.23,'Python',(10+2j)]
print('Original List L: ',L)

#Indexing & Slicing
print('1st Elements: ',L[0])
print('Last Element: ',L[-1])
print('L[0:3]: ',L[0:3])
print('L[::-1]: ',L[::-1])

#Adding & Removining elements
L.append(22)
L.append(33)
print('After adding elements, L: ',L)
L.remove(10)
L.remove((10+2j))
print('After Removing elements, L: ',L)

# Replacing list elements
L[0]='Java'
L[1]='HTML'
print('After replacing, L: ',L)




