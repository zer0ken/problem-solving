def solution(arr):
    s, e = None, None
    for i, num in enumerate(arr):
        if num == 2:
            if s == None:
                s = e = i
            else:
                e = i
    return arr[s:e+1] if s is not None else [-1]