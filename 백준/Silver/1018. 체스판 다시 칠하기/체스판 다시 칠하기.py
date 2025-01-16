import sys

n, m = map(int, input().split())
lines = sys.stdin.read().split()
count = 0

matches = []

for row in range(n):
    need = 'W' if row % 2 == 0 else 'B'
    
    row_matches = []
    for col in range(m):
        row_matches.append(1 if lines[row][col] == need else 0)
        need = 'W' if need == 'B' else 'B'
    matches.append(row_matches)

required_changes = 64

for row in range(7, n):
    for col in range(7, m):
        local_matches = sum(sum(r[col-7:col+1]) for r in matches[row-7 : row+1])
        local_changes = min(local_matches, 64 - local_matches)
        if local_changes < required_changes:
            required_changes = local_changes
            if required_changes == 0:
                break

print(required_changes)