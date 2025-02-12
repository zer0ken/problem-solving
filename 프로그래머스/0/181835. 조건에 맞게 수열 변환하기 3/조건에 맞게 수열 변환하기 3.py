def solution(arr, k):
    return [n * k if k % 2 else n + k for n in arr]