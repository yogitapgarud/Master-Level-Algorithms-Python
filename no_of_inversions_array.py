import sys

def num_inversions(a):
	l = len(a)
	if len(a) <= 1:
		return 0
	else:
		num_inv = 0
		a, num_inv = msort(a, num_inv)
		return num_inv

def msort(a, count):
	if (len(a)) > 1:
		mid = (len(a)) / 2
		left = a[:mid]
		right = a[mid:]

		l, c1 = msort(left, count)
		r, c2 = msort(right, count)
		count = c1 + c2

		i = 0
		j = 0
		k = 0
		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				a[k] = left[i]
				i += 1
			else:
				a[k] = right[j]
				j += 1
				count = count + len(left[i:])
			k += 1
		while i < len(left):
			a[k] = left[i]
			k += 1
			i += 1
		while j < len(right):
			a[k] = right[j]
			k += 1
			j += 1
	return a, count