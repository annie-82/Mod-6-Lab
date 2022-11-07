#=========================================================================================================
#Program Name: Factorial
# Author: Keegan Bramlet
# Date: Novemeber 6, 2022
# Program Purpose: Convert Radians to Degrees
#===============================================================================
n = input("Enter a number: ")
factorial = 1
if int(n) >= 1:
    for i in range (1, int(n)+1):
        factorial = factorial * i
print("Factorail of ", n, " is : ", factorial)

import math
print(math.factorial(int(n)))
