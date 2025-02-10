def solution(arr, n):
    for i in range(0 if len(arr) % 2 else 1, len(arr), 2):
        arr[i] += n
    return arr