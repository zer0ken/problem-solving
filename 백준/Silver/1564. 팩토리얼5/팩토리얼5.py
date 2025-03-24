N = int(input())
factorial = 1
for i in range(2, N + 1):
    factorial = factorial * i
    factorial = int(str(factorial).rstrip('0')[-12:])
print(str(factorial)[-5:])