#break: to break the loop execution based on some condition
# break & continue statements must be inside loop only

for i in range(5):
    if i==3: # if i=3 break statement will execute
        print('Processing is Enough, Break Loop Execution')
        break
    print(f'i:{i}')

# Break statement-2
cart=[20,30,40,500,600,25]
for item in cart:
    if item>=500:
        print(f'To Process this item:{item},subscription must be required')
        break
    print(f'Processing item:{item}')
