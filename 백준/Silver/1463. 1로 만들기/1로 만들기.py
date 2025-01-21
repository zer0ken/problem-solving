import sys
n = int(sys.stdin.readline().rstrip())

limit = n

def dfs(stack):
    global limit
    
    last = stack[-1]
    if last == 1:
        limit = len(stack)
        return 0
    if len(stack) >= limit:
        return n
    
    op_count = []
    if last >= 3 and last % 3 == 0:
        cur = last // 3
        if cur >= 1:
            stack.append(cur)
            op_count.append(dfs(stack))
            stack.pop()
    if last > 2 and last % 2 == 0:
        cur = last // 2
        if cur >= 1:
            stack.append(cur)
            op_count.append(dfs(stack))
            stack.pop()
    cur = last - 1
    stack.append(cur)
    op_count.append(dfs(stack))
    stack.pop()
    
    return min(op_count) + 1

sys.stdout.write(str(dfs([n])))