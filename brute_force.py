# Author: catxu
# Date: 2016-06-29
# Purpose: use Python implement the BF algorithm

#I will fix it later...

def bfAlgo(src, substr):
	i = 0
	count = 0
#	tmp = 24
#	for i in range(0, len(src) - len(substr)):
	while (i <= len(src) - len(substr)):
		j = 0
		while(src[i] == substr[j]):
			i = i + 1
			j = j + 1
			if j == len(substr):
				break;
			elif(j == len(substr) - 1):
				count = count + 1
			else:
				i = i + 1
				j = 0

#		if j == len(substr):
#			break;

	return count

#	for str1 in substr:
#		for str2 in src:
#			if str2 == str1:

srcStr = 'Hope is a good thing. Fear can hold you prisoner, hope can set you free. Get busy living, or get busy dying.'
targetStr = 'set you free'

subIdx = bfAlgo(srcStr, targetStr)

print(subIdx)

