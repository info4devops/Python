s=[x for x in range(1,11)]
v=[x*x for x in range(1,11)]
print(s)
print(v)
m=[x for x in v if x%2==0]
print(m)
dif_ele = [x for x in v if x not in m]
print(dif_ele)
