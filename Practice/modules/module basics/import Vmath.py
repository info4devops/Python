# importing Vmath Module
print('::::::case-1::::::::')
import Vmath
print(Vmath.x)
Vmath.add(100,200)
Vmath.product(11,12)

# Importing module with alias
print('::::::case-2::::::::')
import Vmath as V
print(V.x)
V.add(100,200)
V.product(11,12)

# Importing module types
#1. from Vmath import* 
#2. from Vmath import <a specific function/variable>
#3. import Vmath
#4. import Vmath as V

