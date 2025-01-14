import sys
while True:
    a, b = sys.stdin.readline().rstrip().split()
    if a == b == '0':
        break
    a = int(a)
    b = int(b)
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')