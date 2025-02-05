def solution(string, pattern):
    return string[:string.rindex(pattern) + len(pattern)]