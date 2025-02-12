def solution(arr):
    r, c = len(arr), len(arr[0])
    if r < c:
        arr.extend([0] * c for _ in range(c - r))
    elif r > c:
        for i in range(r):
            arr[i].extend([0] * (r - c))
    return arr