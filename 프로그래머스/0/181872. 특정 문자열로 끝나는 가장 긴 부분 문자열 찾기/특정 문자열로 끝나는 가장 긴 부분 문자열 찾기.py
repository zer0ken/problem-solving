def solution(string, pattern):
    import re
    return re.findall(f'.*(?={pattern})', string)[0] + pattern