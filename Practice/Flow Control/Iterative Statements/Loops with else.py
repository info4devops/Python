#Loops with else block
#With execution else block
cart=[10,20,30,]
for item in cart:
    if item>=500:
        print(f'we cannot process this item:{item}')
        break
    print(f'item processed:{item}')
else:
    print('All Items Processed successfully')
print('\n')

# Without execution else block
print(':::::::::Case-2:::::::::::')
cart = [10, 20, 600,40,]
for item in cart:
    if item >= 500:
        print(f'we cannot process this item:{item}')
        break
    print(f'item processed:{item}')
else:
    print('All Items Processed successfully')

