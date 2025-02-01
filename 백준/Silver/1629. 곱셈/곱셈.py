import sys

A, B, C = map(int, sys.stdin.readline().split())

def power(n, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return n % C
    if exp < 4:
        ret = n
        for _ in range(exp - 1):
            ret = ((ret % C) * (n % C))
        return ret % C
        
    sqrt_exp = int(exp ** 0.5)
    x = power(power(n, sqrt_exp), sqrt_exp) % C
    
    left_exp = exp - sqrt_exp * sqrt_exp
    y = power(n, left_exp) % C
    
    return ((x % C) * (y % C)) % C

sys.stdout.write(str(power(A, B)))