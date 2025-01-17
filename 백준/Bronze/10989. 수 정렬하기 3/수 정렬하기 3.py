import sys

n = int(sys.stdin.readline().rstrip())
counter = [0 for _ in range(10000)]

for _ in range(n):
    counter[int(sys.stdin.readline().rstrip()) - 1] += 1

for i in range(10000):
    count = counter[i]
    for _ in range(count):
        sys.stdout.write(str(i+1) + '\n')