import sys
N, *arr = map(int, sys.stdin.read().rstrip().split())
arr.sort()
sys.stdout.write('\n'.join(map(str, arr)))