# Accessing the each character in a string from both +ve and -ve index
# Accessing using indexing:
s= input('Enter any string: ')
i=0
for x in s:
  print(f'The character Present at Positive index:{i} and at negative index:{i-len(s)} is:{x}')
  i=i+1
print()

# Accessing using slice Operator
print(f's[::] is {s[::]}')
print(f's[::-1] is {s[::-1]}')
print(f's[:1000] is {s[:1000]}')
print(f's[:3] is {s[:3]}')