def solution(arr, i):
    for j in range(i, len(arr)):
        if arr[j] == 1:
            return j
    return -1