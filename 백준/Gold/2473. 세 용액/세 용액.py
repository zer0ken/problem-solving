def main():
    import sys
    
    N, *arr = map(int, sys.stdin.read().split())
    arr.sort()
    
    min_set = arr[:3]
    min_value = abs(sum(min_set))
    
    for i in range(N - 2):
        l = i + 1
        r = N - 1
        
        while l < r:
            value = arr[i] + arr[l] + arr[r]
            
            if min_value > abs(value):
                min_value = abs(value)
                min_set[0] = arr[i]
                min_set[1] = arr[l]
                min_set[2] = arr[r]
            
            if value == 0:
                sys.stdout.write(' '.join(map(str, min_set)))
                return
            elif value < 0:
                l += 1
            else:
                r -= 1

    sys.stdout.write(' '.join(map(str, min_set)))

if __name__ == '__main__':
    main()