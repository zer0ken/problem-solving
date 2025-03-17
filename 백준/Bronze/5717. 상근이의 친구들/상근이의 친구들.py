import sys

*lines, _ = sys.stdin.read().rstrip().splitlines()
for line in lines:
    bf, gf = map(int, line.split())
    sys.stdout.write(f'{bf+gf}\n')