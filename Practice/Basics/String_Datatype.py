s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('s=',s)
print('Type of s: ',type(s))

# Accessing Elements of string
# Using Indexing
print('1st element in s: ',s[0])
print('Last element in s: ',s[-1])
print()

# Using Slicing slice(start,stop,step)
s1=slice(3)
s2=slice(1,10,2)
s3=slice(15,3,-1)
print('s(3):',s[s1])
print('s(1,10,2):',s[s2])
print('s(15,3,-1):',s[s3])


# Array Slicing
print('s[0:]:',s[0:])
print('s[::-1]:',s[::-1])
print('s[0:8]:',s[0:8])
print('s[8:0:-1]:',s[8:0:-1])
print('s[0:10000000]:',s[0:10000000])# wont raise index error








