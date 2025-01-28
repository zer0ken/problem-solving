import sys


def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def is_palindrome(str_n):
    for i in range(len(str_n) // 2):
        if str_n[i] != str_n[-(i + 1)]:
            return False
    return True


N = int(sys.stdin.readline().rstrip())
n = N if N > 2 else 2
while True:
    if is_palindrome(str_n := str(n)) and is_prime(n):
        break
    n += 1

sys.stdout.write(str_n)