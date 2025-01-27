from collections import Counter

def solution(a, b, c, d):
    counter = Counter((a, b, c, d))
    most_common = counter.most_common()
    
    if most_common[0][1] == 4:
        return 1111 * a
    if most_common[0][1] == 3:
        return (10 * most_common[0][0] + most_common[1][0]) ** 2
    if most_common[0][1] == 2:
        if most_common[1][1] == 2:
            return (most_common[0][0] + most_common[1][0]) * abs(most_common[0][0] - most_common[1][0])
        if most_common[1][1] == 1:
            return most_common[1][0] * most_common[2][0]
    return min(a, b, c, d)
    
    
    return answer