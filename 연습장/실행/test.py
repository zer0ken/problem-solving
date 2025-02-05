import sys

n = N = int(sys.stdin.readline())
x = 1
while n > 0:
    n -= x
    x += 1
x -= 1
n += x
if x % 2 == 0:
    sys.stdout.write(f'{n}/{x + 1 - n}\n')
else:
    sys.stdout.write(f'{x + 1 - n}/{n}\n')