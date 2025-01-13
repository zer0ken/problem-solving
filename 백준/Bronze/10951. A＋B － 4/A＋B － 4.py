import sys
while True:
    try:
        a, b = sys.stdin.readline().rstrip().split()
    except:
        break
    else:
        print(int(a) + int(b))