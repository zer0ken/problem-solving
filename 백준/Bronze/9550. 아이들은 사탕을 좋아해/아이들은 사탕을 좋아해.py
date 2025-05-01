import sys

readline = sys.stdin.readline
results = []
for _ in range(int(readline())):
    N, K = map(int, readline().split())
    arr = list(map(int, readline().split()))
    results.append(sum(v // K for v in arr))
print(*results, sep='\n')