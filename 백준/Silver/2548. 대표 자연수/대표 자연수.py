def main():
    import sys
    
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    sys.stdout.write(str(arr[(N - 1) // 2]))


if __name__ == '__main__':
    main()