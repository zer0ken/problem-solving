import sys
from functools import cache
from collections import deque

N = int(sys.stdin.readline().rstrip())

@cache
def matmul(a, b):
    return (
        (
            (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % 1_000_000_007,
            (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % 1_000_000_007
        ),
        (
            (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % 1_000_000_007,
            (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % 1_000_000_007
        )
    )

@cache
def matpow(mat, exp):
    if exp < 4:
        powed = mat
        while exp > 1:
            powed = matmul(powed, mat)
            exp -= 1
        return powed
    
    sqrt_exp = int(exp ** 0.5)
    powed = matpow(matpow(mat, sqrt_exp), sqrt_exp)
    
    left_exp = exp - sqrt_exp * sqrt_exp
    if left_exp > 0:
        powed = matmul(powed, matpow(mat, left_exp))
    
    return powed

if N <= 2:
    sys.stdout.write('1')
else:
    mat = matpow(((0, 1), (1, 1)), N - 1)
    sys.stdout.write(str(mat[1][1]))