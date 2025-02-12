def solution(str_list, ex):
    return ''.join(filter(lambda s: ex not in s, str_list))