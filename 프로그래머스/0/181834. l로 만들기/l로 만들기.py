def solution(string):
    answer = ''
    return ''.join('l' if ord(cha) < ord('l') else cha for cha in string)