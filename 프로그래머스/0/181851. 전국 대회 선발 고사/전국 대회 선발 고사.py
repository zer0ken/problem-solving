def solution(rank, attendance):
    rank = list(filter(lambda x: attendance[x[0]], enumerate(rank)))
    rank.sort(key=lambda x: x[1])
    
    ret = 0
    for i in range(min(3, len(rank))):
        ret = ret * 100 + rank[i][0]
    return ret