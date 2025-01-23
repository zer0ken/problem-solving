import sys

readline = sys.stdin.readline
n = int(readline().rstrip())

stack = []
for _ in range(n):
    op, *args = readline().split()
    if op == 'push':
        stack.append(args[0])
    elif op == 'pop':
        sys.stdout.write(f'{stack.pop() if stack else -1}\n')
    elif op == 'size':
        sys.stdout.write(f'{len(stack)}\n')
    elif op == 'empty':
        sys.stdout.write(f'{1 if not stack else 0}\n')
    elif op == 'top':
        sys.stdout.write(f'{stack[-1] if stack else -1}\n')