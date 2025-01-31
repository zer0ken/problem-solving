import sys

a, b, c = map(int, sys.stdin.read().split())
s = set([a, b, c])
if a + b + c != 180:
    sys.stdout.write('Error')
elif a == b == c:
    sys.stdout.write('Equilateral')
elif len(s) == 2:
    sys.stdout.write('Isosceles')
else:
    sys.stdout.write('Scalene')