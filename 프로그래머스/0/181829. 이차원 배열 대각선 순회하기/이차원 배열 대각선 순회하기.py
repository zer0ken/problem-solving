def solution(board, k):
    return sum(
        board[i][x-i]
        for x in range(k + 1)
        for i in range(x + 1)
        if i < len(board) and (x - i) < len(board[0])
    )