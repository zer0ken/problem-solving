import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
sys.stdout.write(str(min(arr)) + ' ' + str(max(arr)))