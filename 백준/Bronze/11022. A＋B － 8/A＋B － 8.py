import sys
for no in range(1, int(input()) + 1):
    a, b = sys.stdin.readline().rstrip().split()
    sys.stdout.write('Case #'+str(no)+': '+a+' + '+b+' = '+str(int(a)+int(b))+'\n')