import sys
N, *arr = map(int, sys.stdin.read().split())

if N == 1:
    print('A')
    exit(0)

if N == 2:
    print(arr[0] if arr[0] == arr[1] else 'A')
    exit(0)

if arr[0] == arr[1]:
    print(arr[0] if len(set(arr)) == 1 else 'B')
    exit(0)

if arr[1] == arr[2]:
    print(arr[1] if len(set(arr[1:])) == 1 else 'B')
    exit(0)

if (arr[1] - arr[2]) % (arr[0] - arr[1]):
    print('B')
    exit(0)
a = (arr[1] - arr[2]) // (arr[0] - arr[1]) 
b = arr[1] - arr[0]*a

for i in range(1, N):
    if arr[i] != arr[i-1]*a + b:
        print('B')
        exit(0)
else:
    print(arr[-1]*a + b)