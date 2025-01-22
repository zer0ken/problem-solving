import sys
readline = sys.stdin.readline
readline()
a = set(readline().split())
b = set(readline().split())
sys.stdout.write(str(len(a^b)))