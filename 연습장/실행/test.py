def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    edges = [(i,) + tuple(map(int, readline().split())) for i in range(N)]
    s_to_i = []
    s_to_e = []
    for i, s, e in sorted(edges, key=lambda x: x[1]):
        s_to_i.append(i)
        s_to_e.append(e)
    

if __name__ == '__main__':
    main()