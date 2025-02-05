def solution(string):
    arr = list(string.lower())
    for i in range(len(arr)):
        if arr[i] == 'a':
            arr[i] = 'A'
    return ''.join(arr)