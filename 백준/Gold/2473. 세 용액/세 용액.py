def main():
    import sys
    
    N, *arr = map(int, sys.stdin.read().split())
    arr.sort()
    
    min_set = None
    min_value = float('inf')
    
    for i in range(N - 2):
        l = i + 1
        r = N - 1
        
        while l < r:
            value = arr[i] + arr[l] + arr[r]
            
            if min_value > abs(value):
                min_value = abs(value)
                min_set = [arr[i], arr[l], arr[r]]
            if value == 0:
                print(*min_set)
                return
            elif value < 0:
                l += 1
            else:
                r -= 1
    
    print(*min_set)
    

if __name__ == '__main__':
    main()