import sys

N = int(sys.stdin.readline().rstrip())
sieve = [i for i in range(N + 1)]

primes = []
acc = [0]

for num in range(2, N + 1):
    if sieve[num] == -1:
        continue
    primes.append(num)
    if not acc:
        acc.append(num)
    else:
        acc.append(num + acc[-1])
    for kn in range(2 * num, N + 1, num):
        sieve[kn] = -1

l = r = len(acc) - 1
count = 0
while r >= 0:
    l = r - 1
    if acc[r] < N:
        break
    while l >= 0:
        t = acc[r] - acc[l]
        if t == N:
            count += 1
        if t >= N:
            break
        l -= 1
    r -= 1

sys.stdout.write(str(count))