import time


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


def fibit(n):
    return fibitHelper(n, 0, 1)


def fibitHelper(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibitHelper(n-1,b, a+b)


def main():
    start_time = time.time()
    print(fibo(40))
    elapsed_time = time.time() - start_time
    print(elapsed_time)


if __name__ == '__main__':
    main()