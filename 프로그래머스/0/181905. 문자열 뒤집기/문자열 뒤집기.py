def solution(string, s, e):
    return string[:s] + string[s:e + 1][::-1] + string[e + 1:]