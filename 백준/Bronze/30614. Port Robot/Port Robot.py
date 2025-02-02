import sys

sys.stdin.readline()

stack = []
ord_a = ord('a')
for op in sys.stdin.readline().rstrip():
    if ord(op) >= ord_a:
        stack.append(op)
    else:
        op = op.lower()
        if not stack or stack[-1] != op:
            stack.append(None)
            break
        stack.pop()
sys.stdout.write('0' if stack else '1')