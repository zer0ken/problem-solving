import sys

K, *arr = map(int, sys.stdin.read().split())
stack = []
for v in arr:
    if v == 0:
        stack.pop()
    else:
        stack.append(v)
sys.stdout.write(str(sum(stack)))