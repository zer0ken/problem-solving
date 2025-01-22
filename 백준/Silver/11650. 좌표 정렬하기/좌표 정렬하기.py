import sys
readline = sys.stdin.readline
n = int(readline().rstrip())

arr = []
for _ in range(n):
    x, y = map(int, readline().split())
    
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        mid_x, mid_y = arr[mid]
        if x < mid_x or (x == mid_x and y < mid_y):
            r = mid - 1
        else:
            l = mid + 1
    if l >= len(arr):
        arr.append((x, y))
    else:
        arr.insert(l, (x, y))
for x, y in arr:
    sys.stdout.write(f'{x} {y}\n')