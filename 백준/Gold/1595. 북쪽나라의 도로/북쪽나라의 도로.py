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
        
        flag = 0
        for there, d in road[here]:
            if not visited[there]:
                flag = 1
                visited[there] = 1
                get_farthest(there, dist + d)
                visited[there] = 0
        if not flag and max_dist < dist:
            farthest = here
            max_dist = dist
            
    max_dist, farthest = 0, 1
    visited = [0] * 10001
    visited[1] = 1
    get_farthest(1, 0)
    
    visited = [0] * 10001
    visited[farthest] = 1
    get_farthest(farthest, 0)
    
    write(str(max_dist))


if __name__ == '__main__':
     main()