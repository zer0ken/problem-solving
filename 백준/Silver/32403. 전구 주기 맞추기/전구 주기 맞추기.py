def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, T = map(int, readline().split())
    arr = list(map(int, readline().split()))
    
    adjusted = 0
    for v in arr:
        decresed = 0
        while T % (v - decresed):
            decresed += 1
        if v > T:
            adjusted += decresed
        else:
            increased = 0
            while T % (v + increased):
                increased += 1
            adjusted += min(increased, decresed)
    
    write(str(adjusted))
    
if __name__ == '__main__':
    main()