import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

start = -1
count = 0
for i in range(M):
    if start != -1:
        nth = i - start
        if nth % 2 and S[i] == 'I' or nth % 2 == 0 and S[i] == 'O':
            start = -1
            
            length = (nth - 1) // 2
            if length >= N:
                count += length + 1 - N

    if start == -1 and S[i] == 'I':
        start = i

if start != -1:
    length = (i - start) // 2
    if length >= N:
        count += length + 1 - N

print(count)