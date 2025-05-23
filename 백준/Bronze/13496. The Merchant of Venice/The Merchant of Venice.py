import sys
input = sys.stdin.readline

results = []
for x in range(1, int(input()) + 1):
    n, s, d = map(int, input().split())
    total = 0
    for _ in range(n):
        di, vi = map(int, input().split())
        if di <= s * d:
            total += vi
    results.append(f'Data Set {x}:\n{total}\n')
print(*results, sep='\n')