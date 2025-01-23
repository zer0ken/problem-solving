import sys

readline = sys.stdin.readline

t = int(readline().rstrip())
cache = dict()

def dfs(acc, target):
    cache_key = target - acc
    if cache_key in cache:
        return cache[cache_key]
    
    if acc == target:
        cache[cache_key] = 1
        return 1
    if acc > target:
        cache[cache_key] = 0
        return 0
    
    cases = 0
    for add in range(1, 4):
        cases += dfs(acc + add, target)
    
    cache[cache_key] = cases
    return cases


for _ in range(t):
    n = int(readline().rstrip())
    cases = dfs(0, n)
    sys.stdout.write(f'{cases}\n')