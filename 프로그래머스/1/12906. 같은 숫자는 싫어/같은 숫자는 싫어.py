def solution(arr):
    result = []
    for v in arr:
        if not result or result[-1] != v:
            result.append(v)
    return result