import sys

N, M = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))

def dfs(stack=[], depth=0):
    if depth == M:
        sys.stdout.write(' '.join(map(str, stack)) + '\n')
        return
    depth += 1
    for n in arr:
        if n in stack:
            continue
        stack.append(n)
        dfs(stack, depth)
        stack.pop()

dfs()