def fibDyn(n):
	fib1 = 0
	fib2 = 1
	sum = 0
	for i in range(2, n):
		sum = fib1 + fib2
		fib2 = fib1
		fib1 = sum
	return sum


def knapsack(w, weight, val, n):
	l = [[0 for x in range(w + 1)] for y in range(n + 1)]

	for i in range(n + 1):
		for j in range(w + 1):
			if i == 0 or j == 0:
				l[i][j] = 0
			elif weight[i - 1] <= j:
				l[i][j] = max(val[i - 1] + l[i - 1][j - weight[i - 1]], l[i - 1][j])
			else:
				l[i][j] = l[i - 1][j]

	return l[n][w]


def knapsackcontent(w, weight, v, n):
	l = [[0 for x in range(w+1)] for y in range(n+1)]

	for i in range(n+1):
		for j in range(w+1):
			if i == 0 or j == 0:
				l[i][j] = 0
			elif weight[i-1] <= w:
				l[i][w] = max(v[i-1] + l[i-1][w-weight[i-1]], l[i-1][w])
			else:
				l[i][w] = l[i-1][w]

	k = []
	for i in range(n+1):
		for j in range(j+1):
			if l[i][j] != 0:
				k.append(l[i][j])
	return k


def printMaxActivities(s, f):
	n = len(f)
	print
	"The following activities are selected"

	# The first activity is always selected
	i = 0
	print
	i,

	# Consider rest of the activities
	for j in range(n):

		# If this activity has start time greater than
		# or equal to the finish time of previously
		# selected activity, then select it
		if s[j] >= f[i]:
			print(j)
			i = j

	# Driver program to test above function


def main():
	s = [2, 1, 3, 4, 3, 6, 4]
	f = [4, 5, 5, 5, 7, 7, 8]
	printMaxActivities(s, f)


if __name__ == '__main__':
	main()
