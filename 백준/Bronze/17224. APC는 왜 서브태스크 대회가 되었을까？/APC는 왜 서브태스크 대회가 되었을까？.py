def main():
    import sys

    readline = sys.stdin.readline
    
    N, L, K = map(int, readline().split())
    
    scores = {100: 0, 140: 0}
    for i in range(N):
        sub1, sub2 = map(int, readline().split())
        if sub2 <= L:
            scores[140] += 1
            if scores[140] == K:
                break
        elif sub1 <= L:
            scores[100] += 1

    if scores[140] == K:
        print(140 * K)
    else:
        print(140 * scores[140] + 100 * min(K - scores[140], scores[100]))


if __name__ == '__main__':
    main()