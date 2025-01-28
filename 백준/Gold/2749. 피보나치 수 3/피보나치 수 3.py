import sys

N = int(sys.stdin.readline().rstrip())

def matmul(a, b):
    return [
        [
            (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % 1000000,
            (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % 1000000
        ],[
            (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % 1000000,
            (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % 1000000          
        ]  
    ]

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

if N <= 2:
    sys.stdout.write('1')
else:
    mat = matpow(((0, 1), (1, 1)), N - 1)
    sys.stdout.write(str(mat[1][1]))