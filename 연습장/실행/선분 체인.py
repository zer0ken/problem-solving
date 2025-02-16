def main():
    import sys
    from bisect import bisect_left
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    edges = [tuple(map(int, readline().split()))for _ in range(N)]
    edges.sort()
    
    end = []
    cross = [[] for _ in range(N)]
    for i, (s, e) in enumerate(edges):
        k = bisect_left(end, (e, i))
        if k == len(end):
            end.append((e, i))
        else:
            for _, j in end[k:]:
                cross[j].append(i)
                cross[i].append(j),
            end.insert(k, (e, i))
    
    def farthest_from(here, visited, global_visited):
        max_distance = 0
        farthest = here
        
        for there in cross[here]:
            if not visited[there]:
                global_visited[there] = True
                visited[there] = True
                farthest_, distance = farthest_from(there, visited, global_visited)
                visited[there] = False
                
                if max_distance < distance:
                    max_distance = distance
                    farthest = farthest_
                
        return farthest, max_distance + 1
    
    global_visited = [False] * N
    max_diameter = 0
    for i in range(N):
        if global_visited[i]:
            continue
        global_visited[i] = True
        visited = [False] * N
        farthest, _ = farthest_from(i, visited, global_visited)
        visited = [False] * N
        farthest, diameter = farthest_from(farthest, visited, global_visited)
        if max_diameter < diameter:
            max_diameter = diameter
    write(str(max_diameter))


if __name__ == '__main__':
    main()