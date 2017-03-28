import sys

def longest(t):
	if t == []:
		return 0
	else:
		a, b = pf(t)
		return b

def pf(t):
	if t[0] != [] and t[2] != []:
		h1, l1 = pf(t[0])
		h2, l2 = pf(t[2])
		h = 1 + max(h1,h2)
		l = max(h1 + h2 + 2, max(l1, l2))
		print"t[1]: ", t[1], h, l, l1, l2
	elif t[0] != []: 
		h1, l1 = pf(t[0])
		h = 1 + h1
		l = max(h, l1)
		print"t[1]: ", t[1], h, l, l1
	elif t[2] != []:
		h2, l2 = pf(t[2])
		h = 1 + h2
		l = max(h, l2)
		print"t[1]: ", t[1], h, l, l2
	else:
		h = 0
		l = 0

	return h, l
		
			