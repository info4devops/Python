# Tuple Packing
a=10
b=20
t=a,b
print('::::::Tuple Packing::::::')
print(f't:{t}')
print(f'Type of t:{type(t)}')
print()

# Tuple Unpacking
print('::::::Tuple UnPacking::::::')
t1=(11,22,33,44)
p,q,r,s = t1
print(f'p={p} \nq={q} \nr={r} \ns={s}')
print()

print('::::::Tuple UnPacking Using: *args ::::::')
t2=(111,222,333,444)
p,q,*r = t1
print(f'p={p} \nq={q} \nr={r}')
print()
