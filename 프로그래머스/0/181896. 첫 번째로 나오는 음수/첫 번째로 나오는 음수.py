def solution(arr):
    for i, num in enumerate(arr):
        if num < 0:
            return i
    return -1