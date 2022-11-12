#===========================================================================================
#Program Name: Random Int
# Author: Keegan Bramlet
# Date: Novemeber 6, 2022
# Program Purpose: print an odd integer between 0 and 100
#===========================================================================================
import random
int1 = random.randint(0, 100)
if int1 % 2 != 0:
  print(int1)

#make the randomly generated number be odd.
  while True:
    num = random.randint(0, 100)
    if num % 2 != 0:
        break
print("Odd number is", num)




