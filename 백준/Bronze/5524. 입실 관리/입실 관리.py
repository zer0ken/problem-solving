import sys
N, *lines = sys.stdin.read().rstrip().splitlines()
for name in lines:
    sys.stdout.write(name.lower() + '\n')