def solution(n):
    from collections import deque
    arr = [[0] * n for _ in range(n)]
    deltas = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])

    num = 1
    row, col = 0, 0
    while num <= n * n:
        arr[row][col] = num
        num += 1
        
        nrow, ncol = row + deltas[0][0], col + deltas[0][1]
        if 0 <= nrow < n and 0 <= ncol < n and arr[nrow][ncol] == 0:
            row, col = nrow, ncol
        else:
            deltas.rotate(-1)
            row, col = row + deltas[0][0], col + deltas[0][1]
            
    return arr