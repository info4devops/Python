#continue: Skip particular itteration and execute next itteration
#printing odd numbers from 0-5 using continue statement

for i in range(5):
    if i%2==0:
        continue
    print(f'i:{i}')
print('\n')

# Continue statement-2
cart=[20,30,40,500,600,25]
for item in cart:
    if item>=500:
        print(f'To Process this item:{item},subscription must be required')
        continue
    print(f'Processing item:{item}')

#continue statement-3

numbers=[10,20,33,0,44,0,100]
for n in numbers:
    if n==0:
        print(f'skipped:{n},Zero division not possible')
        continue
    print('100/{}={}'.format(n,100/n))



