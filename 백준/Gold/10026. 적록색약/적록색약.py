import sys

n = int(sys.stdin.readline().rstrip())

img = [
    sys.stdin.readline().rstrip()
    for _ in range(n)
]

isolated = 0
isolated_rg = 0

visited = set()
rg_visited = set()

def visit_neighbor(start):
    queue = [start]
    rg_queue = []
    
    visited.add(start)
    rg_visited.add(start)
    
    while queue or rg_queue:
        if queue:
            r, c = queue.pop(0)
            rg_only = False
        else:
            r, c = rg_queue.pop(0)
            rg_only = True
        rm, cm = r - 1, c - 1
        rp, cp = r + 1, c + 1
        pixel = img[r][c]
        
        visiting = (r, c)
        
        for pos in ((r, cm), (r, cp), (rm, c), (rp, c)):
            r_, c_ = pos
            if r_ < 0 or r_ >= n or c_ < 0 or c_ >= n:
                continue
            pixel_ = img[r_][c_]
            if not rg_only and pos not in visited and pixel == pixel_:
                queue.append(pos)
                visited.add(pos)
                rg_visited.add(pos)
            elif pos not in rg_visited and pixel != 'B' and pixel_ != 'B':
                rg_queue.append(pos)
                rg_visited.add(pos)

count = 0
rg_count = 0

for row in range(n): 
    for col in range(n):
        pos = (row, col)
        rgb_isolated = pos not in visited
        rg_b_isolated = pos not in rg_visited
        
        if rgb_isolated:
            count += 1
        if rg_b_isolated:
            rg_count += 1
        
        if rgb_isolated or rg_b_isolated:
            visit_neighbor(pos)

sys.stdout.write(f'{count} {rg_count}')