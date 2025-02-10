def solution(strings):
    from collections import Counter
    counter = Counter(map(len, strings))
    return counter.most_common(1)[0][1]