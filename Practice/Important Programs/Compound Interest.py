# finding compound interest
# A = P(1 + R/100)**t
# CI=A-P

# Taking input from user
P=eval(input('Enter principle amount(P): '))
R=eval(input('Enter rate of interest(R): '))
t=eval(input('Enter time(t) in yrs: '))
Total_amount= P*(1+(R/100))**t
compound_interest= Total_amount-P
print(f'The compound interest is: {compound_interest}')
print(f'Total payable amount: {Total_amount}')