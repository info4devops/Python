# Accessing string characters from both forward and backward direction using while loop.
s= input('Enter any string: ')
n=len(s)
i=0
# forward direction
print('Forward Direction')
while i<n:
  print(s[i],end=" ")
  i=i+1
# Backward Direction
print('\nBackward Direction')

i= -1
while i>=-n:
  print(s[i],end=" ")
  i=i-1
  

    