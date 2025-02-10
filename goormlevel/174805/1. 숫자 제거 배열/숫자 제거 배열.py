import sys
N, K = sys.stdin.readline().split()
sys.stdout.write(str(len(list(filter(lambda s: K not in s, sys.stdin.readline().split())))))