cache = dict()

def bico(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    key = (n, k)
    if key in cache:
        return cache[key]
    
    v = bico(n - 1, k - 1) + bico(n - 1, k)
    cache[key] = v
    return v

n, k = map(int, input().split())
print(bico(n, k))