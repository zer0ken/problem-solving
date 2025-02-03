import sys
from collections import deque

N = int(sys.stdin.readline())
shoelace = [list(map(int, sys.stdin.readline().split()))]
for i in range(1, N):
    shoelace.append(list(map(int, sys.stdin.readline().split())))
shoelace.append(shoelace[0])

red, blue = 0, 0
for i in range(N):
    red += shoelace[i][0] * shoelace[i+1][1]
    blue += shoelace[i][1] * shoelace[i+1][0]
area = abs((red - blue) / 2)
area = int(area * 10 + 0.5) / 10
sys.stdout.write(str(area))