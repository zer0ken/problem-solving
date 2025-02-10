def main():
    import sys

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    arr = list(map(int, readline().split()))
    
    if N == 1:
        write(str(sum(arr) - max(arr)))
        exit(0)
    
    corner = min(
        arr[0]+arr[1]+arr[2], arr[0]+arr[1]+arr[3], arr[1]+arr[2]+arr[5], arr[1]+arr[3]+arr[5],
        arr[3]+arr[4]+arr[5], arr[2]+arr[4]+arr[5], arr[0]+arr[3]+arr[4], arr[0]+arr[2]+arr[4]
    )
    edge = min(
        arr[0]+arr[1], arr[0]+arr[2], arr[0]+arr[3], arr[0]+arr[4],
        arr[1]+arr[2], arr[2]+arr[4], arr[4]+arr[3], arr[3]+arr[1],
        arr[1]+arr[5], arr[2]+arr[5], arr[3]+arr[5], arr[4]+arr[5]
    )
    side = min(arr)
        
    write(str(4 * corner + (8*N - 12) * edge + (5*N**2 - 16*N + 12) * side))


if __name__ == '__main__':
    main()