import sys
t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())

    parts = dict()
    for j in range(n):
        part = sys.stdin.readline().split()[1]
        if part not in parts:
            parts[part] = 1
        else:
            parts[part] += 1

    cases = 1
    for part in parts.values():
        cases *= (part + 1)
    
    sys.stdout.write(str(cases - 1) + '\n')