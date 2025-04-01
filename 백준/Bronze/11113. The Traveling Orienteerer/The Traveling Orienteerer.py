N = int(input())
points = [list(map(float, input().split())) for _ in range(N)]

for _ in range(int(input())):
    M = int(input())
    route = [points[i] for i in map(int, input().split())]
    length = 0
    for i in range(1, M):
        length += ((route[i][0] - route[i-1][0])**2 + 
                   (route[i][1] - route[i-1][1])**2)**0.5
    print(int(length + 0.5))