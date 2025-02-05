import sys

N = int(sys.stdin.readline())
found = 0

vertical = [False] * N
ascending = [False] * (2*N - 1)
descending = [False] * (2*N - 1)

def dfs(i=0):
    global found
    if i == N:
        found += 1
        return
    for j in range(N):
        if vertical[j] or ascending[i + j] or descending[i - j]:
            continue
        vertical[j] = ascending[i + j] = descending[i - j] = True
        dfs(i + 1)
        vertical[j] = ascending[i + j] = descending[i - j] = False

dfs()
sys.stdout.write(str(found))