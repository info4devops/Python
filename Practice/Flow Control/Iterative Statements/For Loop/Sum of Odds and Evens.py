# To find the sum of evens and Odds using for loop

n=int(input('Enter range value: '))
list_of_odds=[]
list_of_evens =[]
sum_of_odds = 0
sum_of_evens = 0

for x in range(n+1):
  # Find out Odd Number
  if (x%2 !=0):
    list_of_odds.append(x)
    sum_of_odds = sum_of_odds+x
  
  # for even number
  else:
    list_of_evens.append(x)
    sum_of_evens = sum_of_evens+x
    
print(f'List of Even Numbers:{list_of_evens}')
print(f'List of Odd Numbers:{list_of_odds}')
print()
print(f'No of Odd Numbers:{len(list_of_odds)}')
print(f'No of Even Numbers:{len(list_of_evens)}')
print()
print(f'The sum of Odd numbers present in 1st {n} Numbers is:{sum_of_odds}')
print(f'The sum of Even numbers present in 1st {n} Numbers is:{sum_of_evens}')
print()

