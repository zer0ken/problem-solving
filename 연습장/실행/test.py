def main():
    import sys
    from bisect import bisect_left
    from collections import defaultdict
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    A = readline().rstrip()
    B = readline().rstrip()
    
    B_inv = defaultdict(list)
    for i, b in enumerate(B):
        B_inv[b].append(i)
    
    lis = []
    for a in A:
        b_inv = B_inv[a]
        if not b_inv:
            continue
        for i in range(len(b_inv) - 1, -1, -1):
            b_idx = b_inv[i]
            idx = bisect_left(lis, b_idx)
            if idx == len(lis):
                lis.append(b_idx)
            else:
                lis[idx] = b_idx
    write(str(len(lis)))


if __name__ == '__main__':
    main()