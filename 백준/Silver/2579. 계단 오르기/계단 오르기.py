import sys

n, *scores = map(int, sys.stdin.read().split())
scores = [0] + scores
cache = {}

def dfs(level=0, force_skip=None):
    cache_key = (level, force_skip)
    if level == n:
        cache[cache_key] = scores[-1]
        return scores[-1]
    if level > n:
        cache[cache_key] = 0
        return 0
    
    if cache_key in cache:
        return cache[cache_key]
    
    score = 0
    
    if not force_skip:
        next_score = dfs(
            level + 1, 
            True if force_skip is not None else False
        )
        if next_score > 0:
            score = next_score + scores[level]
            
    next_score = dfs(level + 2, False)
    if next_score > 0:
        score = max(score, next_score + scores[level])
    
    cache[cache_key] = score
    return score

sys.stdout.write(str(dfs()))