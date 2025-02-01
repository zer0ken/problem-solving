def solution(string):
    counter = [0] * 52
    for cha in string:
        if ord(cha) >= ord('a'):
            counter[26 + ord(cha) - ord('a')] += 1
        else:
            counter[ord(cha) - ord('A')] += 1
    return counter
    
solution('ABCZabcz')