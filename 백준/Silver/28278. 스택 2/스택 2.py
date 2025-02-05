import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    op, *args = map(int, sys.stdin.readline().split())
    match op:
        case 1:
            stack.append(args[0])
        case 2:
            t = stack.pop() if stack else -1
            sys.stdout.write(f'{t}\n')
        case 3:
            sys.stdout.write(f'{len(stack)}\n')
        case 4:
            sys.stdout.write('0\n' if stack else '1\n')
        case 5:
            t = stack[-1] if stack else -1
            sys.stdout.write(f'{t}\n')