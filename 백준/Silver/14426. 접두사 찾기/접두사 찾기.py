def main():
    import sys
    from bisect import bisect_left
    
    lines = iter(sys.stdin.read().rstrip().splitlines())
    
    N, M = map(int, next(lines).split())
    S = sorted(next(lines) for _ in range(N))
    S.sort()
    
    count = 0
    for word in lines:
        idx = bisect_left(S, word)
        if idx < N and S[idx].startswith(word):
            count += 1
    sys.stdout.write(str(count))
    
    
if __name__ == '__main__':
    main()