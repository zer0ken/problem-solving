import sys

x = set()
y = set()
for _ in range(3):
    x_, y_ = map(int, sys.stdin.readline().split())
    x ^= {x_}
    y ^= {y_}
sys.stdout.write(f'{x.pop()} {y.pop()}')