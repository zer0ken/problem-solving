import sys
_, *lines = sys.stdin.read().rstrip().split('\n')
sys.stdout.write('\n'.join(str(sum(map(int, line.split()))) for line in lines))