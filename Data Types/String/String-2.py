# Repeating the string using loops
s=input('Enter any string:')
n=len(s)
i=0
print(f'\nForward Direction')
while i<n:
    print(s[i],end=' ')
    i=i+1
print(f'\nBackward Direction')
i=-1
while i>=-n:
    print(s[i],end=' ')
    i=i-1

# Mathematical Operations on string
s1='Python'
s2='Program'
# concatenation
print(f'\ns1+s2={s1+s2}')
# Repetation
print(f's1*2={s1*2}')
print(f's2*3={s2*3}')