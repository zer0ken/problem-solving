import sys

x = 2
for i in range(int(sys.stdin.readline())):
    x = x * 2 - 1
sys.stdout.write(str(x * x))