import sys

s = [False for _ in range(20)]

for i in range(int(sys.stdin.readline().rstrip())):
    op = sys.stdin.readline()
    
    if op == 'all\n':
        s = [True for _ in range(20)]
        continue
    if op == 'empty\n':
        s = [False for _ in range(20)]
        continue
        
    op, v = op.split()
    v = int(v)

    if op == 'add':
        s[v-1] = True
    elif op == 'remove':
        s[v-1] = False
    elif op == 'check':
        sys.stdout.write('1\n' if s[v-1] else '0\n')
    elif op == 'toggle':
        s[v-1] = not s[v-1]
