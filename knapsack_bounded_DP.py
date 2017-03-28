import sys
from collections import defaultdict

def best(w, a):
	if w < 1:
		return None
	else:
		opt = defaultdict(dict)
		n = len(a)
		back = [[-1 for i in range(n)] for j in range(w+1)] 
		#print back
		for i in range (n):
			opt[0][i] = 0

		for j in range (w+1):
			opt[j][-1] = 0

		sol = [0] * n
		sol2 = [0] * n
		b2 = [-1 for i in range(w+1)]

		for x in range(1, w+1):
			b2[x] = -1 
			for i in range(n):
				opt[x][i] = opt[x][i-1]
				back[x][i] = -1
				for j in range(a[i][2]+1):
					if x >= a[i][0] * j:
						if (opt[x-a[i][0]*j][i-1] + a[i][1]*j) > opt[x][i]:
							opt[x][i] = opt[x-a[i][0]*j][i-1] + a[i][1] * j
							back[x][i] = j
							b2[x] = j
							
		x = w
		i = n-1
		while x > 0 and i > -1:
			if back[x][i] > -1:
				sol[i] = back[x][i]
				x -= a[i][0] * back[x][i]
				i -= 1
				#print "x: ", x
			else:
				i -= 1
				if (i < 0):
					x -= 1
					i = n-1


		return opt[w][n-1], sol