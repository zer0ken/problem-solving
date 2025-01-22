import sys
readline = sys.stdin.readline
n = int(readline().rstrip())

arr = []
for _ in range(n):
    age, name = readline().split()
    age = int(age)
    
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        mid_value = arr[mid]
        if age < mid_value[0]:
            r = mid - 1
        else:
            l = mid + 1
    if l >= len(arr):
        arr.append((age, name))
    else:
        arr.insert(l, (age, name))
for age, name in arr:
    sys.stdout.write(f'{age} {name}\n')