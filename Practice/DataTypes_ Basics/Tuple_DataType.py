# Creating empty tuple
t1=()
print('t1:',t1)
print('Type of t1: ',type(t1))
print()

# Creating single valued tuple: must be ends with comma
t2=(10,)
print('t2:',t2)
print('Type of t2: ',type(t2))

# Tuple Operation
t=(10,'python',22.32,(11+22j))
print('Original tuple,t: ',t)

# Indexing and slicing of tuple
print('1st Elements: ',t[0])
print('Last Element: ',t[-1])
print('L[0:3]=',t[0:3])
print('L[::-1]=',t[::-1])

# adding and removing elements to tuple not possible
# Replacing tuple elements not possible
#t[0]=333 #TypeError: 'tuple' object does not support item assignment

