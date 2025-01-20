import sys

max_value = 0
max_row = 0
max_col = 0
for i in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if row[j] > max_value:
            max_value = row[j]
            max_row = i
            max_col = j
sys.stdout.write(f'{max_value}\n{max_row+1} {max_col+1}')