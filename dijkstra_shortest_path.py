import sys
from collections import defaultdict
from heapdict import *

def shortest(n, _edges):
	edges = defaultdict(list)
	for (u, v, cost) in _edges: # undirected
        	edges[u].append((v, cost))
	        edges[v].append((u, cost))
	
	dist = defaultdict(lambda: float ('inf'))
	dist[0] = 0
	print "dist: ", dist
	prevnode = defaultdict(lambda: -1)
	prevnode[0] = -1
	unvisited = heapdict()
	unvisited[0] = 0

	for i in range(1, n-1):
		unvisited[i] = float ('inf')
	#print "len: ", len(unvisited)
	current = 0
	for j in range(n-1) :
		current, d = unvisited.popitem()
		#print "current: ", current, "d:", d
		for i, (v, c) in enumerate(edges[current]):
			print "current: ", current, "v: ", v 
			ans = dist[current] + c
			if ans < dist[v]:
				print "changing best[v]: ", dist[v], "current: ", current, "v: ", v 
				dist[v] = ans
				prevnode[v] = current
				unvisited[v] = ans
	return dist[n-1], solution(prevnode, n-1)

def solution(back, n):
	print "inside sol"
	v = n
	l = []
	l.append(v)
	while v > 0:
		v = back[v]
		l.append(v)
		print "v:", v

	print "out of while in sol"
	ans = list(reversed(l))
	return ans
