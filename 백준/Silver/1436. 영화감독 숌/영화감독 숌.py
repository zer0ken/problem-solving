import sys

n = int(sys.stdin.readline().rstrip())

value = 666
count = 1
while count < n:
    value += 1
    if '666' in str(value):
        count += 1
sys.stdout.write(str(value))