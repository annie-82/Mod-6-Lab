#=========================================================================================================
#Program Name: Pi
# Author: Keegan Bramlet
# Date: Novemeber 6, 2022
# Program Purpose: Write a program that approximates π  according to the Leibniz’s formula using the following pseudo codes.
#Then compare the result with the value of math.pi in the math module
#=========================================================================================================
pi = 0
denom = 1
for i in range(0, 100000):
    if (i % 2) == 0:
        pi = pi + 4/d
    else:
        pi = pi - 4/d
                            
        denom = denom + 2
             
        print("pi =", pi)

#the pseudo code states 4/d, but "d" is not defined
#I have no idea what to define it as or if it supposed to be something else
