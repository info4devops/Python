a=input('Enter a value:')
b=input('Enter b value:')
#type casting
a=int(a)
b=int(b)
print('value of a>b:',a>b)
print('value of a>=b:',a>=b)
print('value of a<b:',a<b)
print('value of a<=b:',a<=b)

# Relational Operators for string: comparision based on unicode values
s1='PYTHON'
s2='python'
print('s1=',s1,'\ns2=',s2)
print(f'The Unicode value of letter {s1[0]} is:{ord(s1[0])}')
print(f'The Unicode value of letter {s2[0]} is:{ord(s2[0])}')

print('s1>s2:',s1>s2)
print('s1>=s2:',s1>=s2)
print('s1<s2:',s1<s2)
print('s1<=s2:',s1<=s2)

