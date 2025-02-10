import sys
N = int(sys.stdin.readline())
sys.stdout.write(str(oct(int(sum(map(int, sys.stdin.readline().split())))))[2:])