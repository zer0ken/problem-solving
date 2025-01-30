import sys
from bisect import bisect_left

arr = sorted(map(int, sys.stdin.readline().split()))
sys.stdout.write(str(arr[1]))