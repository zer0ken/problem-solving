import sys

T = int(sys.stdin.readline())

N = int(sys.stdin.readline())
acc_A = [0]
for a in map(int, sys.stdin.readline().split()):
    acc_A.append(acc_A[-1] + a)
    
M = int(sys.stdin.readline())
acc_B = [0]
for b in map(int, sys.stdin.readline().split()):
    acc_B.append(acc_B[-1] + b)

valid_sumsub_b = {}
for i in range(N):
    for j in range(i + 1, N + 1):
        v = T - acc_A[j] + acc_A[i]
        if v in valid_sumsub_b:
            valid_sumsub_b[v] += 1
        else:
            valid_sumsub_b[v] = 1

cases = 0
for i in range(M):
    for j in range(i + 1, M + 1):
        sumsub_b = acc_B[j] - acc_B[i]
        if sumsub_b in valid_sumsub_b:
            cases += valid_sumsub_b[sumsub_b]

sys.stdout.write(str(cases))