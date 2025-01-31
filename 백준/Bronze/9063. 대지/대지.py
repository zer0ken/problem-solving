import sys

for i in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    if i == 0:
        x1 = x0 = x
        y1 = y0 = y
        continue
    x0 = x0 if x0 <= x else x
    y0 = y0 if y0 <= y else y
    x1 = x1 if x1 >= x else x
    y1 = y1 if y1 >= y else y
sys.stdout.write(str(abs(x0 - x1) * abs(y0 - y1)))