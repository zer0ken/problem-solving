def solution(arr):
    return arr + [arr[-1] - arr[-2] if arr[-1] > arr[-2] else arr[-1] * 2]