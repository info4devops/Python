s1=input("Enter s1:")
s2=input("Enter s2:")
l1=[]
l2=[]
n=0
# finding order of each element in string1
for i in s1:
    l1.append(ord(i))
    n=n+1
print(f'Order of each character in s1:{l1}')

# finding order of each element in string2
for i in s2:
    l2.append(ord(i))
    n=n+1
print(f'Order of each character in s1:{l2}')

# comparing strings
if s1==s2:
    print(f"Both Strings Are Equal")
elif s1<s2:
    print(f"'{s1}' is LESS THAN '{s2}'")
else:
    print(f"'{s1}' is GREATER THAN '{s2}'")

