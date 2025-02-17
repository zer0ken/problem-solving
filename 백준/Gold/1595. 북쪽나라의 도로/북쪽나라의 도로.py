def main():
    import sys
    
    sys.setrecursionlimit(10000)
    read = sys.stdin.read
    write = sys.stdout.write
    
    road = [[] for _ in range(10001)]
    for line in read().rstrip().splitlines():
        u, v, d = map(int, line.split())
        road[u].append((v, d))
        road[v].append((u, d))
    
    def get_farthest(here, dist):
        nonlocal max_dist, farthest, visited
        
        has_next = False
        for there, d in road[here]:
            if not visited[there]:
                has_next = True
                visited[there] = True
                get_farthest(there, dist + d)
                visited[there] = False
        if not has_next and max_dist < dist:
            farthest = here
            max_dist = dist
            
    max_dist, farthest = 0, 1
    visited = [False] * 10001
    visited[1] = True
    get_farthest(1, 0)
    
    visited = [False] * 10001
    visited[farthest] = True
    get_farthest(farthest, 0)
    
    write(str(max_dist))


if __name__ == '__main__':
     main()