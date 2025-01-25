import sys

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]


op = ['+']
stack = [1]
cur = 2

for value in arr:
    if (not stack and cur > value) or (stack and stack[-1] > value):
        op = None
        break
    while not stack or stack[-1] < value:
        stack.append(cur)
        cur += 1
        op.append('+')
    if stack[-1] == value:
        stack.pop()
        op.append('-')

sys.stdout.write('\n'.join(op) if op else 'NO')