def binary_search(arr, s, e, k):
    arr_ = sorted(arr[s:e+1])
    l, r = 0, len(arr_) - 1
    while l <= r:
        mid = (l + r) // 2
        if k < arr_[mid]:
            r = mid - 1
        else:
            l = mid + 1
    if l == len(arr_):
        return -1
    return arr_[l]

def solution(arr, queries):
    results = []
    for s, e, k in queries:
        results.append(binary_search(arr, s, e, k))
    return results