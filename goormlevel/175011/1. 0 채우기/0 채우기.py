N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            break
    else:
        continue
    break

result = 0
for p in range(N):
    result += board[i][p]
    result += board[p][j]

print(result)