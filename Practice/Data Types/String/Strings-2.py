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

i=-1
while i>=-n:
  print(s[i],end=" ")
  i=i-1

# Accessing Elements using for loop
print('Accessing Using For Loop')
#forward direction
print('\nForward Direction')
for x in s[::1]:
  print(x,end=" ")

# Backward Direction
print('\nBackward Direction')
for x in s[::-1]:
  print(x,end=" ")

  

    