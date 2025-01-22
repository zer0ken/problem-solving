import sys

n, r, c = map(int, sys.stdin.readline().split())
on_same = (r - 1) % 2 == (c - 1) % 2

for r in range(n):
    rmod2 = r % 2
    for c in range(n):
        cmod2 = c % 2
        if on_same:
            sys.stdout.write('v' if rmod2 == cmod2 else '.')
        else:
            sys.stdout.write('v' if rmod2 != cmod2 else '.')
    sys.stdout.write('\n')