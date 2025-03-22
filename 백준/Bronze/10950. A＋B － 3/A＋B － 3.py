import sys

N, *lines = sys.stdin.read().rstrip().splitlines()
sys.stdout.write('\n'.join(str(sum(map(int, line.split()))) for line in lines))