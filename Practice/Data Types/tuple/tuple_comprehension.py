# program about tuple comprehension: finding sum and average of elements present in tuple
#t1=(x for x in range(1,4))
t2=(x**x for x in range(1,4))
for x in t2:
  print(x,end=",")
print(f'\ntyepe of t2:{type(t2)}')


# Finding sum and average
t = eval(input('Enter any tuple:')) #ex: t=(10,20,30)
length=len(t)
sum=0
for x in t:
  sum = sum+x
print(f'The sum:{sum}')
print(f'The Average:{(sum/length)}') # average = (sum/length)
