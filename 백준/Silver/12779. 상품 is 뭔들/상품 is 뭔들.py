import sys

def sqrt(x):
    t = int(x ** 0.5)
    tt = t * t
    if tt == x:
        return t
    if tt < x:
        while t * t <= x:
            t += 1
        return t - 1
    while t * t >= x:
        t -= 1
    return t

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, sys.stdin.readline().split())
total = b - a
count = sqrt(b) - sqrt(a)
if count == 0:
    sys.stdout.write('0')
else:
    gcd_ = gcd(total, count)
    sys.stdout.write(f'{count//gcd_}/{total//gcd_}')