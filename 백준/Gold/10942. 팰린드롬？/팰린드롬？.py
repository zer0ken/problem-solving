import sys

N = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
M = int(sys.stdin.readline())

is_palindrome = [[True if e <= s else None for e in range(N)] for s in range(N)]

for center in range(N):
    for d in range(1, N):
        s = center - d
        e = center + d
        if s < 0 or e >= N:
            break
        is_palindrome[s][e] = arr[s] == arr[e] and is_palindrome[s+1][e-1]

for center in range(N):
    for d in range(N):
        s = center - d
        e = center + d + 1
        if s < 0 or e >= N:
            break
        is_palindrome[s][e] = arr[s] == arr[e] and is_palindrome[s+1][e-1]

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    s -= 1
    e -= 1
    sys.stdout.write('1\n' if is_palindrome[s][e] else '0\n')