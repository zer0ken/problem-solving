def solution(my_string, overwrite_string, s):
    e = s + min(len(my_string), len(overwrite_string))
    return my_string[:s] + overwrite_string[:e] + my_string[e:]