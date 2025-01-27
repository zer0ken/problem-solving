import sys

N, K = map(int, sys.stdin.readline().split())
sieve = [n for n in range(2, N + 1)]
removed = 0
done = False

for i in range(N - 1):
    if sieve[i] == -1:
        continue
    n = sieve[i]
    for kn in range(n, N + 1, n):
        if sieve[kn - 2] != -1:
            removed += 1
            if removed == K:
                done = True
                break
            sieve[kn - 2] = -1
    if done:
        break

sys.stdout.write(str(kn))