from collections import deque

N, K = map(int, input().split())
q = deque([])
for _ in range(N):
    op, *args = input().split()
    if op =='push':
        if len(q) == K:
            print('Overflow')
        else:
            q.append(args[0])
    elif not q:
        print('Underflow')
    else:
        print(q.popleft())