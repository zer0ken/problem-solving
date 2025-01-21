import sys
n = int(sys.stdin.readline().rstrip())

cache = dict()
def dfs(target):
    if target == 0:
        cache[target] = 1
        return 1
    if target < 0:
        cache[target] = 0
        return 0
        
    cases = 0
    for add in (1, 2):
        next_target = target - add
        if next_target in cache:
            cases += cache[next_target] * add
        else:
            cases += dfs(next_target) * add
    
    cache[target] = cases % 10007
    return cases

for m in range(5, n, 5):
    dfs(m)

sys.stdout.write(str(dfs(n) % 10007))