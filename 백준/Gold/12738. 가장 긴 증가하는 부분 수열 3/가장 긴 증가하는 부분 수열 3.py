import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for num in map(int, sys.stdin.readline().split()):
    if not arr or arr[-1] < num:
        arr.append(num)
        continue
    
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if num == arr[mid]:
            l = mid
            break
        elif num < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    arr[l] = num
    

sys.stdout.write(str(len(arr)))