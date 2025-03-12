import sys

N = int(input())
sum_dist = N**2 -2*N + 1
print(sum_dist)
for i in range(2, N + 1):
    sys.stdout.write(f'{1} {i}\n')