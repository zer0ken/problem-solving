import sys
input = sys.stdin.readline
def BOJ_1654():
    K, N = map(int,input().split())

    cable = [int(input()) for _ in range(K)]

    low, high = 1, sum(cable)//N*2
    
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        n= sum([c//mid for c in cable])
        if n >= N:
            ans = max(0, mid)
            low = mid + 1
        elif n < N:
            high = mid - 1
    print(ans)
BOJ_1654()