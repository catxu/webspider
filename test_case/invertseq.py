# Purpose: inverse typed string
# Author: catxu
# Date: 2016-06-28

i = 0

def invertStr(str):
	if str[i] is not '#':
		invertStr(str[i + 1:])
	if str[i] is not '#':
		print(str[i], end='')

print('Start')
str = input()

invertStr(str)

print('\n' + 'Done!')

# Postscript: use the Python recursive to implementation the inverse string is highly counterintuitive,
# The main idea is to convert the string into a series character array to processing.

def fac(n):
        if n==0 or n==1:
                return 1
        else:
                return n*fac(n-1)

print(fac(3))

print('OK, look good for me')
