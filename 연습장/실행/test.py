def solution(n, build_frame):
    PILLAR = 0
    CEIL = 1
    
    board = [[[False, False] for _ in range(n + 1)] for _ in range(n + 1)]
    
    def is_pillar_safe(x, y):
        if y == 0:
            return True
        if board[x][y-1][PILLAR]:
            return True
        if board[x][y][CEIL]:
            return True
        if x != 0 and board[x-1][y][CEIL]:
            return True
        return False
        
    def is_ceil_safe(x, y):
        if board[x][y-1][PILLAR]:
            return True
        if board[x+1][y-1][PILLAR]:
            return True
        if x != 0 and board[x-1][y][CEIL] and board[x+1][y][CEIL]:
            return True
        return False
    
    for x, y, is_ceil, is_build in build_frame:
        if is_ceil:
            if is_build:
                if is_ceil_safe(x, y):
                    board[x][y][CEIL] = True
            else:
                board[x][y][CEIL] = False
                if (
                    (board[x][y][PILLAR] and not is_pillar_safe(x, y))
                    or (board[x+1][y][PILLAR] and not is_pillar_safe(x + 1, y))
                    or (board[x+1][y][CEIL] and not is_ceil_safe(x + 1, y))
                    or (x != 0 and board[x-1][y][CEIL] and not is_ceil_safe(x -1, y))
                ):
                    board[x][y][CEIL] = True
        elif is_build:
            if is_pillar_safe(x, y):
                board[x][y][PILLAR] = True
        else:
            board[x][y][PILLAR] = False
            if (
                (board[x][y+1][PILLAR] and not is_pillar_safe(x, y + 1))
                or (board[x][y+1][CEIL] and not is_ceil_safe(x, y + 1))
                or (x != 0 and board[x-1][y+1] and not is_ceil_safe(x - 1, y + 1))
            ):
                board[x][y][PILLAR] = True
        
        print('===')
        for y in range(n, -1, -1):
            for x in range(n + 1):
                print('|' if board[x][y][PILLAR] else '.', end='')
                print('_' if board[x][y][CEIL] else ' ', end='')
            print()
            
        print()
        
    structures = []
    for x in range(n + 1):
        for y in range(n + 1):
            if board[x][y][PILLAR]:
                structures.append([x, y, PILLAR])
            if board[x][y][CEIL]:
                structures.append([x, y, CEIL])
        
    return structures

solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[3,2,1,1],[4,2,1,1]])