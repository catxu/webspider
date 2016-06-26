# Author: catxu
# Date: 2016-06-26
# Purpose: generator 100 million random number.

import random

def myRandom():
	items = [x for x in range(1000000)]
	random.shuffle(items)

print('Start...')
myRandom()
print('Done!')