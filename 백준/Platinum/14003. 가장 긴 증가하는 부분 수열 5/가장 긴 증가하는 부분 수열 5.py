import sys
from bisect import bisect_left
from collections import deque

N = int(sys.stdin.readline().rstrip())
arr = []
backtrack = {}

for i, num in enumerate(map(int, sys.stdin.readline().split())):
    if not arr or arr[-1][1] < num:
        backtrack[(i, num)] = arr[-1] if arr else None
        arr.append((i, num))
        continue
    
    l, r = 0, len(arr)
    while l <= r:
        mid = (l + r) // 2
        if arr[mid][1] == num:
            l = mid
            break
        if arr[mid][1] > num:
            r = mid - 1
        else:
            l = mid + 1
    arr[l] = (i, num)
    backtrack[(i, num)] = arr[l - 1] if l - 1 >= 0 else None

lis = deque()
cur = arr[-1]
while cur != None:
    lis.appendleft(cur[1])
    cur = backtrack[cur]
    
sys.stdout.write(f'{len(arr)}\n{" ".join(map(str, lis))}')