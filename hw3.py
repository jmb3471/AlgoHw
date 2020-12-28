import math

def searchHelp(a, v, l, h):
	m = l + math.floor((h-l)/2)
	if l > h:
		return False
	elif v == a[m]:
		return True
	elif v < a[m]:
		return searchHelp(a, v, l, m - 1)
	elif v > a[m]:
		return searchHelp(a, v, m+1, h)


def search(a, v):
	return searchHelp(a, v, 0, a.len() - 1)


def sortedHasSum(s, n, x):
	i = 0
	k = n - 1
	while i < k:
		if (s[i] + s[k] == x):
			return True
		elif (s[i] + s[k] < x):
			i += 1
		else:
			k -= 1
	return False


def mergeSort(s):
	length = len(s)
	if length > 1:
		m = length//2
		left = s[:m]
		right = s[m:]

		mergeSort(left)
		mergeSort(right)

		i = 0
		j = 0
		k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				s[k] = left[i]
				i += 1
			else:
				s[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			s[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			s[k] = right[j]
			j += 1
			k += 1
	return s


def hasSum(s, n, x):
	s = mergeSort(s)
	i = 0
	k = n - 1
	while i < k:
		if (s[i] + s[k] == x):
			return True
		elif (s[i] + s[k] < x):
			i += 1
		else:
			k -= 1
	return False


def partition(s, l, h):
	i = l-1
	pivot = s[h]

	for j in range(l, h):
		if s[j] <= pivot:
			i += 1
			s[i], s[j] = s[j], s[i]

	s[i+1], s[h] = s[h], s[i+1]

	return i+1

def quicksort(s, l, h):
	while (l < h):
		p = partition(s, l, h)

		if ((p - l )< (h - p)):
			quicksort(s, l, p-1)
			l = p + 1
		else:
			quicksort(s, p+1, h)
			h = p - 1

	return s


