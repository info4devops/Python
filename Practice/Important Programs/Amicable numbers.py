#checking amicable numbers
# sum of divisors of n1 (excluding n1) is equal to n2 Ex: 220 & 284

# Input the number
num1 = int(input("Enter value of num1: "))
num2 = int(input("Enter value of num2: "))
l1=[]
l2=[]

#Finding divisors of N1

for i in range(1, num1 + 1):
    if num1 % i == 0:
        # excluding particular number from divisors
        if i == num1:
            continue
        # Adding divisors to list
        l1.append(i)

# Print the divisors
print(f"Divisors of {num1} are:{l1}")

#Finding divisors of num2

for i in range(1, num2 + 1):
    if num2 % i == 0:
        # excluding particular number from divisors
        if i == num2:
            continue
        # Adding divisors to list
        l2.append(i)

# Print the divisors
print(f"Divisors of {num2} are:{l2}")


#finding the sum of divisors
print(f'sum of divisors of num1:{sum(l1)}')
print(f'sum of divisors of num2:{sum(l2)}')


# checking amicable numbers

if sum(l1)==num2 and sum(l2)==num1:
    print(f'\n{num1} and {num2} are amicable numbers')
else:
    print(f'\n{num1} and {num2} are not amicable numbers')




