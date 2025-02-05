def solution(arr):
    return list(filter(lambda s: 'ad' not in s, arr))