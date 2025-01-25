def solution(arr, queries):
    for l, r in queries:
        arr[l], arr[r] = arr[r], arr[l]
    return arr