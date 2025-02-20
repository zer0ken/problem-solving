def main():
    import sys
    from bisect import bisect_left
    import heapq
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    wires = [tuple(map(int, readline().split())) for _ in range(N)]
    wires.sort()
    A = set(list(zip(*wires))[0])
    
    backtrack = {}
    lis = []
    for s, e in wires:
        wire = (e, s)
        idx = bisect_left(lis, wire)
        if idx == len(lis):
            lis.append(wire)
        else:
            lis[idx] = wire
        backtrack[wire] = lis[idx - 1] if idx > 0 else None
    
    cur = lis[-1]
    while cur is not None:
        A.remove(cur[1])
        cur = backtrack[cur]
    
    write(f'{len(A)}\n{"\n".join(map(str, A))}')


if __name__ == '__main__':
    main()