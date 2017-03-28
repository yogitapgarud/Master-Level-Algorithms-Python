import sys
from itertools import repeat
from collections import defaultdict

def max_wis(a, opt = {}):
	if a == []:
		return 0, a
	elif len(a) == 1:
		return a[0], a
	else:
		#opt[0] = a[0]
		opt[-1] = 0
		opt[-2] = 0
		j = 0
		back = []
		back.append(a[0])
		n = len(a)
		d = [[] for i in repeat(None, n)]
		d[0] = [a[0]]
		
		if a[0] < 0:
			d[0] = []
		else:
			d[0] = [a[0]]
		for i in range (n):
			if opt[i-1] > a[i] + opt[i-2]:
				opt[i] = opt[i-1]
				if(i > 0):
					d[i] = d[i-1]
			else:
				opt[i] = a[i] + opt[i-2]
				if i > 1:
					d[i] = d[i-2] + [a[i]]
				elif i == 1:
					d[i] = [a[i]]
		return opt[n-1], d[i]

