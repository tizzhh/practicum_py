def fib(n: int) -> int:
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    inp = int(input())
    print(fib(inp))
