import sys

N = int(sys.stdin.readline().rstrip())
sieve = [n for n in range(2, 1003002)]
primes = []

for i in range(1003002 - 2):
    if sieve[i] == -1:
        continue
    n = sieve[i]
    primes.append(n)
    
    for kn in range(2 * n, 1003002, n):
        sieve[kn - 2] = -1

for prime in primes:
    if prime < N:
        continue
    
    str_prime = str(prime)
    is_palindrome = True
    for i in range(len(str_prime) // 2):
        if str_prime[i] != str_prime[-(i + 1)]:
            is_palindrome = False
            break
    if is_palindrome:
        break

sys.stdout.write(str_prime)
