def solution(sizes):
    answer = max(map(max, sizes)) * max(map(min, sizes))
    return answer