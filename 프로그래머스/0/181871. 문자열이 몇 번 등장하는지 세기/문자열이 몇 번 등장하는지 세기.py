def solution(string, pattern):
    import re
    return len(re.findall(f'(?={pattern})', string))