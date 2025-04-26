def main():
    import sys

    readline = sys.stdin.readline
    
    N, L, K = map(int, readline().split())
    
    difficulties = [tuple(map(int, readline().split())) for _ in range(N)]
    difficulties.sort(key=lambda x: x[1], reverse=True)
    
    score = 0
    while K > 0 and difficulties:
        sub1, sub2 = difficulties.pop()
        if sub1 <= L:
            score += 140 if sub2 <= L else 100
            K -= 1
    
    print(score)


if __name__ == '__main__':
    main()