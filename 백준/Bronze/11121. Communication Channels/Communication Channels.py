import sys
arr = sys.stdin.read().split()
for i in range(1, len(arr), 2):
    print('OK' if arr[i] == arr[i+1] else 'ERROR')