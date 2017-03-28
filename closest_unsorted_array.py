import sys
import math
import decimal
from random import randint

#count = 0
def find(a, x, k):
	if a == []:
		return []
	else:
		
		b = [abs(i-x) for i in a ]
		#print b
		z = qselect(k, b)
		#print "z: ", z
		g = []
		if z != None:
			i = 0
			print "z: ", z
			i = 0
			nc = k
			count = 0
			while(i < len(a)):
				if(b[i] < z):
					count += 1
				i += 1
			eq = k - count
			#print "eq: ", eq
			i = 0
			while((nc > 0) and (i < len(a))):
				if (abs(a[i]-x)) < z:
					g.append(a[i])
					#print "inside elif a[i], i :", a[i], i
					nc -= 1
					i += 1
				elif (abs(a[i]-x) == z) and  (eq > 0):					
					g.append(a[i])
					#print "if, eq: ", eq
					#print "inside if a[i], i :", a[i], i
					eq -= 1
					nc -= 1
					i += 1
				else:
					#print "inside else a[i], i :", a[i], i
					i += 1
		return g


def qselect(k, n):
        if n == [] or k < 1 or k > len(n):
        	return None
   	else:
		#print "n in qselect: ", n
        	pindex = randint(0, len(n)-1)
        	n[0],n[pindex] = n[pindex],n[0]
	        pivot = n[0]
        	left = [x for x in n if x < pivot]
	        right = [x for x in n[1:] if x >=  pivot]
        	lleft = len(left)
	        return pivot if k == lleft+1 else \
        		qselect(k, left) if k <= lleft else \
            		qselect(k-lleft-1, right)
