def solution(s):
    return sorted([s[-i:] for i in range(1, len(s) + 1)])