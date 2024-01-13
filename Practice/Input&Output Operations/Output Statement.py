# Type of output statement
#1. print without argument
print() # print new line character

#2.print with string
print('Hello World')
print()

#3.print withvariable number of arguments
a,b,c=10,20,30
print('The Entered values:',a,b,c) # separates with space
print()

#4. print with specified separator
a,b,c=11,22,33
print('The Entered values:',a,b,c)
print(a,b,c,sep=':')# separates with space
print()

#5.print with variable number of arguments with end attribute
print('pyhton',end=':::')
print('Program',end=':::')
print('Language',end=':::')
print('\n')

# print with object(i.e., list, tuple,set etc)
l=[10,20,30]
t=(11,22,33)
print(l)
print(t)


