N = int(input())
factorial = 1
for i in range(2, N + 1):
    factorial = int(str(factorial * i).rstrip('0')[-12:])
print(str(factorial)[-5:])