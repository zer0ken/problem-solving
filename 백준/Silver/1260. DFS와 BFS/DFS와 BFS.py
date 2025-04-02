import sys

input = sys.stdin.readline


def dfs(v):
    vstd[v] = True
    smap[v].sort()
    result.append(v)
    for i in smap[v]:
        if not vstd[i]:
            dfs(i)

def bfs(v):
    queue = [v]
    vstd[v] = True
    result.append(v)
    while queue:
        d = queue.pop(0)
        for i in smap[d]:
            if not vstd[i]:
                queue.append(i)
                vstd[i] = True
                result.append(i)

N,M,V = map(int,input().split())
smap = [[] for i in range(N+1)]
vstd = [False] * (N+1)
result = []
for i in range(M):
    a,b = map(int, input().split())
    smap[a].append(b)
    smap[b].append(a)

dfs(V)
print(*result)
result = []
cnt = 1
vstd = [False] * (N+1)
bfs(V)
print(*result)