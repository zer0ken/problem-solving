import sys

N, B = map(int, sys.stdin.readline().split())
MAT = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(N)
]


def matmul(a, b):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 10000
    return result


def matpow(a, exp):
    if exp <= 1:
        return a
    if exp < 4:
        ret = a
        while exp > 1:
            ret = matmul(ret, a)
            exp -= 1
        return ret
    
    sqrt_exp = int(exp ** 0.5)
    ret = matpow(matpow(a, sqrt_exp), sqrt_exp)
    
    left_exp = exp - sqrt_exp * sqrt_exp
    if left_exp > 0:
        ret = matmul(ret, matpow(a, left_exp))
    
    return ret

result = matpow(MAT, B)
for i in range(N):
    for j in range(N):
        result[i][j] %= 1000
for row in result:
    sys.stdout.write(f'{" ".join(map(str, row))}\n')