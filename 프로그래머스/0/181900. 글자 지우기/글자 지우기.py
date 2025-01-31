def solution(string, indices):
    copy = list(string)
    for i in sorted(indices, reverse=True):
        del copy[i]
    return ''.join(copy)