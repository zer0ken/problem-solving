def solution(str1, str2):
    str3 = ''
    for c1, c2 in zip(str1, str2):
        str3 += c1 + c2
    return str3