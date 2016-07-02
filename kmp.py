# Author: catxu
# Date: 2016-07-02
# Purpose: use Python implement the KMP algorithm

#def getNextIdx(patternStr):

def genNext(pattern, next):
	i = 0
	j = 0
	next[0] = -1
	for i in range(0, len(pattern)):
		if j == 0 or pattern[i] == pattern[j]:	#求得第 i 个元素的 next[] 数组的下标，ig: pattern[2] == pattern[0] next[3] = 1
			i = i + 1
			j = j + 1
			next[i] = j
		else:
			j = next[j]

	return next

def getKmpIdx(targStr, srcStr, next):
	i = 0
	j = 0
	index = -1

	while targStr[j] == '\0' or srcStr == '\0':
		if srcStr[i] == targStr[j]:
			i = i + 1
			j = j + 1
		else:
			j = next[j]
			if j == -1:
				i = i + 1
				j = j + 1

	if j == len(srcStr):
		index = i - len(targStr) + 1
	return index


srcStr = 'ababaababcb'
targStr = 'ababc'
next = range(5)

#for i in range(0, len(targStr)):
#	print(i)

#print(next)

indexArr = genNext(targStr, next)
index = getKmpIdx(targStr, srcStr, indexArr)

print(index)