import sys
import timeit

def best(w, a):
	s = timeit.default_timer()
	if w < 1:
		return None
	else:
		opt = {}
		opt[0]= 0
		n = len(a)
		back = [0] * (w+1)
		sol = [0] * n
		for x in range(1, w+1):
			opt[x] = opt[x-1]
			back[x] = -1
			for i in range(n):
				if x >= a[i][0]:
					if (opt[x-a[i][0]] + a[i][1]) > opt[x] :
						opt[x] = opt[x-a[i][0]] + a[i][1]
						back[x] = i
					elif ((opt[x-a[i][0]] + a[i][1]) == opt[x]) and back[x] == -1 :
						opt[x] = opt[x-a[i][0]] + a[i][1]
						back[x] = i
					
		j = w
		while j > 0:
			if back[j] > -1:
				sol[back[j]] += 1", a[back[j]]
				j -= a[back[j]][0]
			else:
				j -= 1

		e = timeit.default_timer() - s
		return opt[w], sol

#best(58, [(5, 9), (9, 18), (6, 12)])