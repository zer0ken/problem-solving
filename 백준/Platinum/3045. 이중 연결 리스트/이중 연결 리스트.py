def main():
    import sys
    from collections import deque
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    
    next = [i + 1 for i in range(N + 2)]
    next[-1] = None
    
    prev = [i - 1 for i in range(N + 2)]
    prev[0] = None
    
    for _ in range(M):
        op, x, y = readline().split()
        x, y = int(x), int(y)
        
        # pop x
        x_prev = prev[x]
        x_next = next[x]
        prev[x_next] = x_prev
        next[x_prev] = x_next
        if op == 'A':
            # insert x before y
            y_prev = prev[y]
            next[y_prev] = x
            prev[y] = x
            next[x] = y
            prev[x] = y_prev
        else:
            # insert x after y
            y_next = next[y]
            prev[y_next] = x
            next[y] = x
            prev[x] = y
            next[x] = y_next

    backtrack = [0] * (N + 1)
    lis = []
    cur = next[0]
    while cur <= N:
        idx = bisect_left(lis, cur)
        if idx == len(lis):
            lis.append(cur)
        else:
            lis[idx] = cur
        backtrack[cur] = lis[idx - 1] if idx > 0 else None
        cur = next[cur]

    used = [0] * (N + 1)
    cur = lis[-1]
    while cur is not None:
        used[cur] = 1
        cur = backtrack[cur]
    
    write(f'{N - len(lis)}\n')
    
    temp = []
    for v in range(1, N + 1):
        if not used[v]:
            temp.append(v)
        elif temp:
            temp.append(v)
            for i in range(len(temp) - 2, -1, -1):
                write(f'A {temp[i]} {temp[i + 1]}\n')
            temp.clear()
    t = lis[-1]    
    for w in temp:
        write(f'B {w} {t}\n')
        t = w


if __name__ == '__main__':
    main()