import sys

lines = sys.stdin.read().rstrip().split('\n')
for line in lines[:-1]:
    a, b = line.split()
    sys.stdout.write(str(int(a) + int(b)) + '\n')