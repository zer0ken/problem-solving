def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    arr = list(map(int, readline().split()))
    S = int(readline())
    
    desc_arr = sorted(arr, reverse=True)
    used = [0] * N
    
    cur = 0
    while S > 0 and cur < N:
        for desc_idx, num in enumerate(desc_arr):
            if used[desc_idx]:
                continue
            idx = arr.index(num)
            if idx - cur <= S:
                S -= idx - cur
                arr.insert(cur, arr.pop(idx))
                used[desc_idx] = 1
                break
        cur += 1
    write(' '.join(map(str, arr)))


if __name__ == '__main__':
    main()