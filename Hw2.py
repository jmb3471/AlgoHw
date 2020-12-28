
def fibPow(n):
	L = [[1, 1], [1, 0]]
	matrix = matrix_power(L, L, n)
	return matrix[1][0]

def matrix_power(m, l, n):
		result = [[0,0],[0,0]]
		if n == 1:
			return m
		for i in range(2):
			for j in range(2):
				for k in range(2):
					result[i][j] += m[i][k] * l[k][j]
		return matrix_power(result, l, n-1)

def main():
	print(fibPow(900))


if __name__ == '__main__':
	main()