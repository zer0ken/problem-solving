def solution(n, slicer, arr):
    a, b, c = slicer
    if n == 1:
        return arr[:b+1]
    if n == 2:
        return arr[a:]
    if n == 3:
        return arr[a:b+1]        
    return arr[a:b+1:c]