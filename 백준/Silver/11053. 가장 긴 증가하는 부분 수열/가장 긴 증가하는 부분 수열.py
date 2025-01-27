import sys
from bisect import bisect_left

N = int(sys.stdin.readline().rstrip())
arr = []

for num in map(int, sys.stdin.readline().split()):
    if not arr or arr[-1] < num:
        arr.append(num)
        continue
    arr[bisect_left(arr, num)] = num
sys.stdout.write(str(len(arr)))