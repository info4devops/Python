# Accessing string elements by using indexing and slicing
# By Using indexing
s=input('Enter Any String:')
i=0
for x in s:
    print(f'The Character present at positive index:{i} & at Negative index:{i-len(s)} is:{x}')
    i=i+1

# Accessing Elements by using Slicing
print('\nby Using Slicing')
print(f's[0]:{s[0]}')
print(f's[0:3]:{s[0:3]}')
print(f's[1:10000]:{s[1:10000]}') # slice operator wont raise index error
print(f's[3:]:{s[3:]}')
print(f's[::-1]:{s[::-1]}')

# Reversing the string by using slice operator
alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(f'Alphabets in NORMAL order:{alphabets}')
print(f'Alphabets in REVERSE order:{alphabets[::-1]}')