#===========================================================================================
#Program Name: Random Range 
# Author: Keegan Bramlet
# Date: Novemeber 6, 2022
# Program Purpose: print 10 random integers between 25 and 
#===========================================================================================
import random
range1 = random.randrange(25, 35, 1)
for rand_num in [random.randrange(25, 35, 1) for i in range(10)]:
  print(rand_num)



