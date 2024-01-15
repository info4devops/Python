# Print the available amicable numbers in the given range
# example: 220 &284

# Get the upper limit from user
limit = int(input("Enter the upper limit to print amicable numbers: "))

# This loop will check for amicable numbers
for a in range(1, limit + 1):
    # Find the sum of proper divisors of 'a'
    sum1 = 0
    for i in range(1, (a // 2) + 1):
        if a % i == 0:
            sum1 = sum1+ i

    # Check if the sum of divisors of 'sum1' equals 'a'
    # and also make sure they're not the same number
    sum2 = 0
    for j in range(1, (sum1 // 2) + 1):
        if sum1 % j == 0:
            sum2 =sum2+ j

    if sum2 == a and a != sum1:
        print(a, sum1)

