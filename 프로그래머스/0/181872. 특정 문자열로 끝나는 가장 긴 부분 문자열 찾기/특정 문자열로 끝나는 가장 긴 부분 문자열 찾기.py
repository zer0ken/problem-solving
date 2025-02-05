def solution(string, pat):
    max_i = 0
    for i in range(len(pat) - 1, len(string)):
        if string[:i+1].endswith(pat):
            max_i = i
    return string[:max_i+1]