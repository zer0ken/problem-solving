def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    
    A_inv = [0] * 2001
    B_inv = [0] * 2001
    for i, a in enumerate(A):
        A_inv[a] = i
    for i, b in enumerate(B):
        B_inv[b] = i
    
    W = int(readline())
    wires = [tuple(map(int, readline().split())) for _ in range(W)]
    wires.sort(key=lambda w: B_inv[w[1]], reverse=True)  
    wires.sort(key=lambda w: A_inv[w[0]])
    
    lis = []
    for a, b in wires:
        idx = bisect_left(lis, B_inv[b])
        if idx == len(lis):
            lis.append(B_inv[b])
        else:
            lis[idx] = B_inv[b]
    
    write(str(W - len(lis)))


if __name__ == '__main__':
    main()