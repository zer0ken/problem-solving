import sys
w = sys.stdin.read().rstrip().split().count('W')
print([-1, 3, 3, 2, 2, 1, 1][w])