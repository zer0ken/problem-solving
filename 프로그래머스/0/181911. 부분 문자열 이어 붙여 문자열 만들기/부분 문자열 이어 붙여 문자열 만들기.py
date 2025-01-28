def solution(strs, parts):
    results = []
    for s, (l, r) in zip(strs, parts):
        results.append(s[l:r+1])
    return ''.join(results)