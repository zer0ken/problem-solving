def solution(rc, operations):
    from collections import deque
    
    N, M = len(rc), len(rc[0])
    
    first_col = deque([rc[i][0] for i in range(N)])
    last_col = deque([rc[i][-1] for i in range(N)])
    rows = deque([deque(rc[i][1:-1]) for i in range(N)])
    
    for op in operations:
        if op == 'ShiftRow':
            first_col.rotate()
            rows.rotate()
            last_col.rotate()
        else:
            rows[0].appendleft(first_col.popleft())
            last_col.appendleft(rows[0].pop())
            rows[-1].append(last_col.pop())
            first_col.append(rows[-1].popleft())
    
    for i in range(N):
        rc[i][0] = first_col[i]
        rc[i][-1] = last_col[i]
        for j in range(1, M - 1):
            rc[i][j] = rows[i][j-1]
        
    return rc