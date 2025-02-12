def solution(string):
    return string.translate(str.maketrans('abcdefghijk', 'lllllllllll'))