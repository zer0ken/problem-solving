import sys
n = int(sys.stdin.readline().rstrip())

cache = dict()
def dfs(acc):
    cache_key = n - acc
    
    if acc == n:
        cache[cache_key] = 1
        return 1
    if acc > n:
        cache[cache_key] = 0
        return 0
        
    cases = 0
    for add in (1, 2):
        next_acc = acc + add
        next_cache_key = n - next_acc
        if next_cache_key in cache:
            cases += cache[next_cache_key]
        else:
            cases += dfs(acc + add)
    
    cache[cache_key] = cases % 10007
    return cases

for m in range(n - 3, -1, -3):
    dfs(m)

sys.stdout.write(str(dfs(0) % 10007))