import sys
readline = sys.stdin.readline


vertices = int(readline().rstrip())
edges = int(readline().rstrip())

graph = dict()
for _ in range(edges):
    p, q = readline().split()
    if p not in graph:
        graph[p] = list() 
    graph[p].append(q)
    if q not in graph:
        graph[q] = list()
    graph[q].append(p)

def dfs(stack=['1'], visited=[]):
    here = stack[-1]
    visited.append(here)
    for there in graph.get(here, []):
        if there in visited:
            continue
        stack.append(there)
        dfs(stack, visited)
        stack.pop()

visited = []
dfs(['1'], visited)
sys.stdout.write(str(len(visited) - 1))