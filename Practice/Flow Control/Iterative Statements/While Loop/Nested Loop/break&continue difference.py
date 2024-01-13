# Netsted Loop
print('Normal Nested Loop')
for i in range(3):
    for j in range(2):
        print(f'i:{i} and j:{j}')
print('\n')

# break
print('Break Statement')
for i in range(3):
    for j in range(4):
        if i==j: # breaks all iteration after this condition met
            break
        print(f'i:{i} and j:{j}')
print('\n')

# Continue
print('Continue Statement')
for i in range(3):
    for j in range(4):
        if i==j: #skipped this
            continue
        print(f'i:{i} and j:{j}')

