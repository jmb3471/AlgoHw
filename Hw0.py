import math


def r(lst):
    if lst == []:
        return []
    else:
        return r(lst[1:]) + [lst[0]]


def prod(m, n):
    if m == 0:
        return 0
    else:
        return prod(m-1,n) + n


#double check on
def fastPow(b, k):
    if k == 0:
        return 1
    elif k%2 == 0:
        return fastPow(b * b, k//2)
    elif ((k + 1)%2 == 0):
        return fastPow(b * b, k//2) * b


def prodAccum(m, n, a):
    if m == 0:
        return a
    else:
        return prodAccum(m-1,n, n+a)

def o_plus(a, b):
    if (b == None):
        return None
    else:
        return a + b


def min(a, d):
    if (a == None and d != None):
        return d
    elif (d == None and a != None):
        return a
    elif a < d:
        return a
    elif a > d:
        return d
    else:
        return None


def minChange(a, d):
    if a == 0:
        return 0
    elif d == []:
        return None
    else:
        if d[0] > a:
            return minChange(a, d[1:])
        else:
            return min(o_plus(1, minChange(a - d[0], d)), minChange(a, d[1:]))


def greedyMinChange(a, d):
    if a == 0:
        return 0
    elif d == []:
        return None
    else:
        if d[0] > a:
            return greedyMinChange(a, d[1:])
        else:
            q = a//d[0]
            r = a%d[0]
            return o_plus(q, greedyMinChange(r, d[1:]))


def powIt(n, b):
    a = 1
    while n != 0:
        a = a * b
        n -= 1
    return a

def main():
    print(fastPow(2,5))

if __name__ == '__main__':
    main()