# finding simple interest
# SI = (PTR/100)

# Taking input from user
P=eval(input('Enter principle amount(P): '))
R=eval(input('Enter rate of interest(R): '))
T=eval(input('Enter time(T) in yrs: '))

simple_interest=(P*T*R)/100
print(f'The simple interest is: {simple_interest}')
Net_payble_amount=P+simple_interest
print(f'Total payble amount: {Net_payble_amount}')