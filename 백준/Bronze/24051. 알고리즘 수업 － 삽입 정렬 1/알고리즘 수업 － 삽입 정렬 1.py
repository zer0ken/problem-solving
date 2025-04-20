def main():
    import sys
    
    N, K, *arr = map(int, sys.stdin.read().split())
    
    count = 0
    last = None
    for i in range(1, N):
        loc = i - 1
        new_item = arr[i]
        
        while 0 <= loc and new_item < arr[loc]:
            count += 1
            arr[loc+1] = arr[loc]
            loc -= 1
            
            if count == K:
                print(arr[loc+1])
                return

        if loc + 1 != i:
            count += 1
            arr[loc + 1] = new_item

            if count == K:
                print(arr[loc + 1])
                return
    
    print('-1')


if __name__ == '__main__':
    main()