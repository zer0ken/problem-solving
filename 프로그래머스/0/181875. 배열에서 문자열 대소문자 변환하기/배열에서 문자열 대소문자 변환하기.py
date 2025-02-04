def solution(arr):
    return [string.lower() if i % 2 == 0 else string.upper() for i, string in enumerate(arr)]