def solution(arr):
    for i, cha in enumerate(arr):
        if cha == 'l':
            return arr[:i]
        if cha == 'r':
            return arr[i+1:]
    return []