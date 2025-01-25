import sys

lines = []
while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    stack = []
    failed = False
    for cha in line:
        if cha in ('(', '['):
            stack.append(cha)
        elif cha == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                failed = True
                break
        elif cha == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                failed = True
                break
    if failed or stack:
        sys.stdout.write('no\n')
    else:
        sys.stdout.write('yes\n')