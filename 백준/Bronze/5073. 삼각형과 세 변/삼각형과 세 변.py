import sys

while True:
    a, b, c = sorted(map(int, sys.stdin.readline().split()))
    if a == b == c == 0:
        break
    s = set([a, b, c])
    if a + b <= c:
        sys.stdout.write('Invalid\n')
    elif a == b == c:
        sys.stdout.write('Equilateral\n')
    elif len(s) == 2:
        sys.stdout.write('Isosceles\n')
    else:
        sys.stdout.write('Scalene\n')