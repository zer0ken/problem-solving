cache = dict()

def fibo(n):
    if n in cache:
        return cache[n]
    if n == 0:
        result = (0, 1, 0)
        cache[0] = result
        return result
    if n == 1:
        result = (1, 0, 1)
        cache[1] = result
        return result
    fibo0, x0, y0 = fibo(n - 1)
    fibo1, x1, y1 = fibo(n - 2)
    result = (fibo0 + fibo1, x0 + x1, y0 + y1)
    cache[n] = result
    return result


n = int(input())
for _ in range(n):
    print(*(fibo(int(input()))[1:]))
