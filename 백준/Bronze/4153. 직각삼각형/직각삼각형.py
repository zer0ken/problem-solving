import sys
while True:
    line = sys.stdin.readline()
    if line[0] == '0':
        break
    a, b, c = map(int, line.split()) 
    aa = a * a
    bb = b * b
    cc = c * c
    
    if aa + bb == cc or aa + cc == bb or bb + cc == aa:
        sys.stdout.write('right\n')
    else:
        sys.stdout.write('wrong\n')
        