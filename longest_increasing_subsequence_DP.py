import sys
from collections import defaultdict

def lis(a):
	if len(a) < 2:
		return a
	else:
		n = len(a)
		#print "len: ", n
		opt = defaultdict(lambda: 1)
		back = defaultdict(lambda: -1)
		max = 1

		for i in range(n):
			#print "i:", i
			for j in range(i):
				if a[j] < a[i]:
					ans = opt[j] + 1
					if ans > opt[i]:
						opt[i] = opt[j] + 1
						back[i] = j
					if ans > opt[max]:
						#print "ans > max, i", ans, max, i
						max = i

		return solution(a, back, max)

def solution(a, back, max):
	i = max
	sol = []
	while i > -1:
		sol.append(a[i])
		i = back[i]
	sol.reverse()
	return "".join(sol)







