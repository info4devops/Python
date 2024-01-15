def convert_to_words(number):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return ones[number]

def convert_teens(number):
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    return teens[number - 1]

def convert_tens(number):
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    return tens[number]

def convert_units(number):
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return units[number]

# Get user input
num = int(input("Enter a number (0-9999999999): "))

# Check if the number is within the valid range
if 0 <= num <= 9999999999:
    # Convert each part of the number to words using if-else statements
    billions = num // 1000000000
    num %= 1000000000

    millions = num // 1000000
    num %= 1000000

    thousands = num // 1000
    num %= 1000

    hundreds = num // 100
    num %= 100

    tens = num // 10
    units = num % 10

    # Print the words for each part
    if billions > 0:
        print(f"{convert_to_words(billions)} Billion", end=" ")

    if millions > 0:
        print(f"{convert_to_words(millions)} Million", end=" ")

    if thousands > 0:
        print(f"{convert_to_words(thousands)} Thousand", end=" ")

    if hundreds > 0:
        print(f"{convert_to_words(hundreds)} Hundred", end=" ")

    if tens > 0 or units > 0:
        if tens == 1:
            # Handle numbers between 10 and 19 separately
            print(convert_teens(units))
        else:
            # Print the words for tens and units place
            print(f"{convert_tens(tens)} {convert_units(units)}")
else:
    print("Invalid input. Please enter a number between 0 and 9999999999.")
