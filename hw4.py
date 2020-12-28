def max2(a, b):
	c = a-b
	k = (c >> 31) & 0x1
	return a - k * c


def fselect(lst, i):
	if len(lst) == 0:
		return None
	x = lst[0]

	l = []
	s = []
	m = []
	for e in lst:
		if e < x:
			l.append(e)
		elif e == x:
			s.append(e)
		else:
			m.append(e)
	l_len = len(l)
	s_len = len(s)
	if i < l_len:
		return fselect(l, i)
	elif i >= l_len and (i < l_len + s_len):
		return x
	else:
		return fselect(m, i - (l_len+s_len))

def partition(s, l, h):
	i = l-1
	pivot = s[h]

	for j in range(l, h):
		if s[j] <= pivot:
			i += 1
			s[i], s[j] = s[j], s[i]

	s[i+1], s[h] = s[h], s[i+1]

	return i+1


def iSelect(lst, i):
	length = len(lst)
	index = partition(lst, 0, len(lst)-1)
	if i < index:
		return iSelectHelper(lst,i, 0, index)
	elif i == index:
		return lst[index]
	else:
		return iSelectHelper(lst, i-index, index, length)
	print(lst)

def iSelectHelper(lst, i, l, h):
	lst = lst[l:h]
	if len(lst) == 0:
		return None

	length = len(lst)
	index = partition(lst, 0, len(lst) - 1)
	if i < index:
		return iSelectHelper(lst, i, 0, index)
	elif i == index:
		return lst[index]
	else:
		return iSelectHelper(lst, i-index, index, length)


def main():
	print(iSelect([10,4,5,8,6,11,26], 5))

if __name__ == '__main__':
	main()
