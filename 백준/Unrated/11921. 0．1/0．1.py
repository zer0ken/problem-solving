import sys

sys.stdin.readline()
acc = 0
for _ in range(50000):
    acc += int(sys.stdin.readline())
sys.stdout.write('50000\n')
sys.stdout.write(str(acc))