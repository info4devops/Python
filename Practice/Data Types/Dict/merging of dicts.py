d1 = {100:'a',200:'b'}
d2 ={300:'X',400:'Y'}

# Merging only keys
result1 ={*d1,*d2}
print('reslut1={*d1,*d2}:',result1)

# Merging only values
result2 ={*d1.values(),*d2.values()}
print('reslut1={*d1.values(),*d2.values()}:',result2)

# Merging entire dict
result3 ={**d1,**d2}
print('reslut1={**d1,**d2}:',result3)