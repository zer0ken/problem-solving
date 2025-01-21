import sys

readline = sys.stdin.readline

n = int(readline().rstrip())
arr = list(map(int, readline().split()))
sarr = {v: i for i, v in enumerate(sorted(set(arr)))}

sys.stdout.write(' '.join([str(sarr[v]) for v in arr]))