def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    switches = list(map(int, readline().split()))
    bulbs = list(map(int, readline().split()))
    indices = {s: i for i, s in enumerate(switches)}
    wires = []
    for s, b in zip(switches, bulbs):
        wires.append((indices[s], indices[b]))
    wires.sort()
    
    backtrack = {}
    lis = []
    for _, e in wires:
        idx = bisect_left(lis, e)
        if idx == len(lis):
            lis.append(e)
        else:
            lis[idx] = e
        backtrack[e] = lis[idx - 1] if idx > 0 else None
    
    to_push = []
    cur = lis[-1]
    while cur is not None:
        to_push.append(switches[cur])
        cur = backtrack[cur]
    to_push.sort()
    write(f'{len(lis)}\n{" ".join(map(str, sorted(to_push)))}')


if __name__ == '__main__':
    main()