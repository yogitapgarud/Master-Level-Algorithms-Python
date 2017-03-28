import sys
import operator
from collections import defaultdict

def order(n, _edges):
	if n < 1:
		return None
	else:
		edges = defaultdict(list)
		indeg = defaultdict(int)

    		for (u, v) in _edges:
		        edges[u].append(v)
			indeg[v] += 1

		l = []
		for i in range(n):
			if i in indeg:
				continue
			else:
				l.append(i)
		#print "sorted_x: ", sorted_x

		topol_order = []
		while l != []:
			current = l.pop(0)
			topol_order.append(current)
			for _, nn in enumerate(edges[current]):
				indeg[nn] -= 1
				if indeg[nn] == 0:
					l.append(nn)

		return topol_order if len(topol_order) == n else 'None'
			 
		
		

		

		