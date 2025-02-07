def solution(string):
    return sorted(filter(lambda s: s.strip(), string.split('x')))