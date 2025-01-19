import sys

n, m = map(int, sys.stdin.readline().split())
acc = [0]

for i, v in enumerate(map(int, sys.stdin.readline().split())):
    acc.append(acc[-1] + v)
    
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{acc[j] - acc[i-1]}\n')