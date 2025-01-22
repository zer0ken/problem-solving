import sys

n = int(sys.stdin.readline().rstrip())
if n < 10:
    n *= 10

count = 0
d = n
while True:
    count += 1
    d1, d2 = d // 10, d % 10
    d3 = d1 + d2
    d = d2 * 10 + d3 % 10
    if d == n:
        break
sys.stdout.write(str(count))