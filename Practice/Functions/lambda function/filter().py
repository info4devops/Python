# WAP to filter even number in given sequence
# Without lambda function
print(':::::::Without lambda function:::::::::::')
def is_even(x):
  if x%2==0:
    return True
  else:
    return False
l1=[10,11,12,13,14,15,16,17]
output=list(filter(is_even,l1))
print(f'Even numbers present in list are:{output}')

# With lambda function
print(':::::::Without lambda function:::::::::::')
l=[10,11,12,13,14,15,16,17]
l_even = list(filter(lambda n:n%2==0,l))
l_odd = list(filter(lambda n:n%2!=0,l))
print(f'Even numbers present in list are:{l_even}')
print(f'Odd numbers present in list are:{l_odd}')



