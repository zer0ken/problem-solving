import sys
readline = sys.stdin.readline
n = int(readline().rstrip())

arr = [int(readline().rstrip()) for _ in range(n)]
sys.stdout.write('\n'.join(map(str, sorted(arr))))