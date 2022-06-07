def fast_fib(n, lookup):
    if not n in  lookup:
        lookup[n] = fast_fib(n - 1, lookup) + fast_fib(n - 2, lookup)
    return lookup[n]


def fib(n):
    lookup = {0:1, 1:1}
    return fast_fib(n, lookup)

if __name__ == '__main__':
    n1 = 100
    n2 = 5

    print(fib(n1), fib(n2))