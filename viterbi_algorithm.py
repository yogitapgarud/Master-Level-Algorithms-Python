import sys

import operator
from collections import defaultdict

def longest(n, _edges):
	if n < 2 or len(_edges) < 1:
		return None
	else:
		edges = defaultdict(list)
		indeg = defaultdict(int)
		dist = defaultdict(lambda: float('-inf'))
		back = defaultdict(lambda: -1)

    		for (u, v) in _edges: # undirected
		        edges[u].append(v)
			indeg[v] += 1

		l = []
		for i in range(n):
			if i in indeg:
				continue
			else:
				l.append(i)
				dist[i] = 0

		topol_order = []
		while l != []:
			current = l.pop(0)
			topol_order.append(current)
			for _, nn in enumerate(edges[current]):
				indeg[nn] -= 1
				if indeg[nn] == 0:
					l.append(nn)
		
		max = float('-inf')
		maxv = -1
		for i, v in enumerate(topol_order):
			#print "inside topol order: ", i, v
			ans = dist[v] + 1
			current = v
			for _, nn in enumerate(edges[current]):
				if dist[nn] < ans:
					#print "**changing dist** v: ", v, "nn:", nn, "ans: ", ans 
					dist[nn] = ans
					back[nn] = v
					if max < ans:
						max = ans
						maxv = nn
		return max, solution(edges, dist, back, maxv)

def solution(edges, dist, back, maxv):
	lp = []
	lp.append(maxv)
	while back[maxv] != -1:
		maxv = back[maxv]
		lp.append(maxv)

	anslp = list(reversed(lp))
	return anslp