# map() function with lambda
# Doubling the numbers present in list
print(':::::::Without lambda function:::::::::::')

l1=[10,11,12,13,14,15,16,17]
def doubleit(x):
  return 2*x # for squares: x*x
output = list(map(doubleit,l1))
print(f'Doubled values:{output}')

print(':::::::With lambda function:::::::::::')
l1=[10,11,12,13,14,15,16,17]
output = list(map(lambda x:2*x,l1))
print(f'Doubled values:{output}')

# map(lambda x,y:x*y,list1,list2) here x is from list1 and y is from list2
# Both list length should be same otherwise it will ignore the extra elements while printing o/p

l1=[1,2,3]
l2=[4,5,6,7,8]
output = list(map(lambda x,y:x*y,l1,l2))
print(f'map() function for 2 lists:{output}')

