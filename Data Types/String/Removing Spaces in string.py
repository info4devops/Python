# Functions for removing strings [rstrip(),lstrip(),strip()]
city=input('Enter city name:')
# strip() : remove spaces from both sides
scity=city.strip()
if scity=='Hyderabad':
    print(f'Hello,Hyderabadi...AAdab')
elif scity=='Bangaluru':
    print(f'Hello,Kannadiga..Namaskara')
else:
    print(f"Your entered city '{city}' is invalid")

