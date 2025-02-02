def solution(arr):
    return max(sum(arr[::2]), sum(arr[1::2]))