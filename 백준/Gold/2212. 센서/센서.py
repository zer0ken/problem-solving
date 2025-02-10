def main():
    import sys
    from collections import deque

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    K = int(readline())
    arr = list(map(int, readline().split()))
    arr.sort()
    sum_dist = arr[-1] - arr[0]
    dist = [arr[i + 1] - arr[i] for i in range(N - 1)]
    dist.sort()
    for _ in range(min(K - 1, N - 1)):
        sum_dist -= dist.pop()
    write(str(sum_dist))


if __name__ == '__main__':
    main()