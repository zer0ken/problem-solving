def solution(string, alp):
    arr = list(string)
    for i in range(len(arr)):
        if arr[i] == alp:
            arr[i] = alp.upper()
    return ''.join(arr)