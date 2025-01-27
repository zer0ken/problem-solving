def solution(my_string, queries):
    arr = list(my_string)
    for s, e in queries:
        arr[s:e+1] = arr[e:s-1 if s > 0 else None:-1]
    return ''.join(arr)