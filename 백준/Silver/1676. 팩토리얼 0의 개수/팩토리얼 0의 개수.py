import sys

n = int(sys.stdin.readline().rstrip())

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

count_0 = 0
for cha in str(factorial(n))[::-1]:
    if cha != '0':
        break
    count_0 += 1
sys.stdout.write(str(count_0))