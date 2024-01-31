f=open('abc.txt','w')
print(f'Name of the file:{f.name}')
print(f'Mode:{f.mode}')
print(f'Is Readable:{f.readable()}')
print(f'Is Writable:{f.writable()}')
print(f'Is Closed:{f.closed}')
f.close()
print(f'Is Closed:{f.closed}')


