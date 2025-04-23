K = int(input())

for i in range(1, K + 1):
    arr = list(map(int, input().split()[1:]))
    arr.sort()
    
    print(
        f'Class {i}\n'
        f'Max {arr[-1]}, Min {arr[0]}, Largest gap '
        f'{max(b - a for a, b in zip(arr, arr[1:]))}'
    )