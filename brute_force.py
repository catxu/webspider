# Author: catxu
# Date: 2016-06-29
# Purpose: use Python implement the BF algorithm

#I will fix it later...

# 2016-06-30, OK, it works!

def bfAlgo(src, substr):
	i = 0
	j = 0
	index = -1

#	for i in range(0, len(src) - len(substr)):
	while (i <= (len(src) - len(substr))):
#		j = 0
#		i = i + 1
		while(src[i] == substr[j]):
#			i = i + 1
#			j = j + 1
			# The relationship between index & length..
			if j == len(substr) - 1:
				index = i - len(substr) + 1;
				return index
#			elif(j == len(substr) - 1):
#				index = index + 1
#			else:
#				i = i + 1
			# matching continue
			i = i + 1
			j = j + 1

#		if index == i - len(substr) + 1:
#			break;

#		if j is not 0:
		# unmatched, backtracking...
		j = 0
		i = i + 1

	return index

#	for str1 in substr:
#		for str2 in src:
#			if str2 == str1:

srcStr = 'Hope is a good thing. Fear can hold you prisoner, hope can set you free. Get busy living, or get busy dying.'
targetStr = 'set you free'
#srcStr = 'beautifully'
#targetStr = 'ul'

subIdx = bfAlgo(srcStr, targetStr)

#print(len(srcStr))
#print(len(targetStr))
#print(len('Hope is a good thing. Fear can hold you prisoner, hope can '))

#print(targetStr[0])

print(subIdx)