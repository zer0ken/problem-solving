def main():
    import sys
    
    read = sys.stdin.read
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    edges = []
    for line in read().rstrip().splitlines():
        a, b, c = map(int, line.split())
        edges.append([a, b, c])
    
    edges.sort(key=lambda e: e[2], reverse=True)
    
    root = [x for x in range(N + 1)]
    root[0] = 1
    
    def get_root(x):
        if root[x] != x:
            root[x] = get_root(root[x])
        return root[x]
    
    sum_c = 0
    cc = N
    
    while cc > 2:
        a, b, c = edges.pop()
        
        root_a = get_root(a)
        root_b = get_root(b)
        
        if root_a != root_b:
            if root_a < root_b:
                root[root_b] = root_a
            else:
                root[root_a] = root_b
            sum_c += c
            cc -= 1
    
    write(str(sum_c))


if __name__ == '__main__':
    main()