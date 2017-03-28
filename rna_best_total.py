import sys
from collections import defaultdict

def best(a):
	n = len(a)
	opt = defaultdict(int)
	back = defaultdict(lambda: -2)
	pairs = set(["AU", "CG", "GU", "UA", "GC", "UG"])
	for d in range(2, n+1):
		i = 0
		j = i + d
		while j < n+1:
			print "a[i]+a[j-1]", a[i]+a[j-1]
			max = float ('-inf')
			for k in range(i+1,j):
				ans = opt[i,k] + opt[k,j]					
				if max <= ans:
					max = ans
					back[i,j] = k
					print "back: ", back[i,j]
			if a[i]+a[j-1] in pairs:
				ans = 1 + opt[i+1, j-1]
				if max <= ans:
					max = ans
					back[i,j] = -1			#tuple((i,-1,j-1))
					print "back: ", back[i,j]

			opt[i,j] = max
			i += 1
			j += 1

	l = ['.'] * n

	def solution(i, j):
		if i < j or back[i,j] > -2:
			k = back[i,j]
			if k == -1:
				l[i] = '('
				l[j-1] = ')'
				for d in range(i+1, j-1):
					l[d] = '.'
				solution(i+1, j-1)
			else:
				if opt[i,k] > 0:
					solution(i,k)
				if opt[k,j] > 0:
					solution(k,j)

	solution(0, n)
	print "l: ", l
	return opt[0,n], "".join(l)

def total(a):
	n = len(a)
	opt = defaultdict(lambda: 1)
	outpair = defaultdict(int)
	back = defaultdict(lambda: -2)
	pairs = set(["AU", "CG", "GU", "UA", "GC", "UG"])
	sum = 1
	for d in range(2, n+1):
		i = 0
		j = i + d
		while j < n+1:
			print "a[i]+a[j-1]", a[i]+a[j-1]
			sum = 0
			lo = set()
			for k in range(i+1,j):
				s = opt[i,k]
				t = opt[k,j]
				ans = s + t
				count = 0
				flag = 0
				#for z in range(i, k-1):
					if a[i]+a[k-1] in pairs:
						if (i,k-1) not in lo:
							print "not in lo: ", (i,k-1)
							print "lo: ", lo
							lo.add(tuple((i,k-1)))
							if opt[k,j] == 1:
								sum += 1
							else:
								sum += 2 * (opt[k,j] - 1)
							count += 1
							flag = 1
				if flag == 0 and k == i+1:
					for r in range(k, j-1):
						for p in range(r+1, j-1):
							if a[r]+a[p] in pairs:
								print "r, p, adding right pairs: ", r, p, a[r]+a[p]
								lo.add(tuple((r, p)))
					sum += opt[k,j] - 1
			if a[i]+a[j-1] in pairs:
				print "**got end pairs**", "a[i]+a[j-1]", a[i]+a[j-1]
				ans = 1 + opt[i+1, j-1]
				sum += ans
			else:
				sum += 1
			opt[i,j] = sum

			i += 1
			j += 1
			print lo
	print lo
	print opt
	return sum

	


