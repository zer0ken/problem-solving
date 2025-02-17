N = int(input())
arr = list(map(int, input().split()))
arr.sort()

acc = [0]
for x in arr:
    acc.append(acc[-1] + x)

total_diff = float('inf')
best = arr[0]
for i, x in enumerate(arr):
    new_total_diff = (i*x - acc[i]) + (acc[-1] - acc[i + 1] - (N - i - 1) * x)
    if total_diff > new_total_diff:
        total_diff = new_total_diff
        best = x
    elif total_diff < new_total_diff:
        break 

print(best)