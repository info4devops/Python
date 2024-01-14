# To find out the area of circle using math module
# area of circle: pi*r**2

from math import *
r = eval(input('Enter Radius of circle:'))
# eval(): To evaluate the type of value

Area_of_circle = pi*r**2
print(f'Area of circle is equal to:{Area_of_circle}')

print(f'Using Math Module: Area of circle is equal to:{pi*pow(r,2)}')