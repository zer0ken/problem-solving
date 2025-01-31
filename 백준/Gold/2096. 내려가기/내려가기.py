import sys
from collections import deque

N = int(sys.stdin.readline())
max_score = [0, 0, 0]
min_score = [0, 0, 0]

r, c = -1, 1
for _ in range(N):
    board = list(map(int, sys.stdin.readline().split()))
    
    max_score[0], max_score[1], max_score[2] = (
        max(max_score[0], max_score[1]) + board[0], 
        max(max_score[0], max_score[1], max_score[2]) + board[1], 
        max(max_score[1], max_score[2]) + board[2]
    )
    min_score[0], min_score[1], min_score[2] = (
        min(min_score[0], min_score[1]) + board[0], 
        min(min_score[0], min_score[1], min_score[2]) + board[1], 
        min(min_score[1], min_score[2]) + board[2]
    )

sys.stdout.write(f'{max(max_score)} {min(min_score)}')