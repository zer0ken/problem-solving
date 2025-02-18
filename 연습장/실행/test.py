def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    edges = [tuple(map(int, readline().split())) for i in range(N)]
    edges.sort()
    
    edges_1 = []
    edges_2 = []
    
    max_end = -1
    for i, (start, end) in enumerate(edges):
        if max_end > end:
            edges_2.append(i)
        else:
            edges_1.append(i)
            max_end = end
    
    
    

if __name__ == '__main__':
    main()