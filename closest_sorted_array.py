import sys
import bisect

def find(a, x, k):
	if a == [] or k <= 0:
		return None
	elif len(a) < k:
		print "not enough elements, so whole list will be printed"
		return a
	else:
		n = len(a)
		p = bisect.bisect(a, x)
		#print "p: ", p
	    	left = l = p - 1
    		right = r = p
		#print "p = ", p, left
		
		
		if( l < 0 ):
			return a[0:k]
		elif( r > (len(a)-1) ):
			s = len(a) - k
			#print "s: ", s
			return a[s:len(a)]
		else:
    			count = 0

    			while (l >= 0 and r < n and count < k):
				#print "inside while"
		        	if ((x - a[l]) <= (a[r] - x)):
					left = l
					l -= 1
					if((right-left+1) > k):
						right = left + k - 1
		        	else:
					right = r
					r += 1
					#print "inside else", right
					if((right-left+1) > k):
						left = right - k + 1
			        count += 1
 
	    		while (count < k and l >= 0):
				left = l
				l -= 1
				#print "inside left only while: ", left
				count += 1

     			while (count < k and r < n):
				right = r
				r += 1
				#print "inside right only while: ", right
				count += 1

			#print" a: ", a[left]
			return a[left:(right+1)]