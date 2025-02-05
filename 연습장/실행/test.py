import sys

N, K = map(int, sys.stdin.readline().split())
compressed = []
count = {}
for num in map(int, sys.stdin.readline().split()):
    if compressed and compressed[-1][0] == num:
        compressed[-1][1] += 1
    else:
        compressed.append([num, 1])
        count[num] = 0
        
max_count = 0
for i in range(len(compressed)):
    num  = compressed[i][0]
    count_num = 0
    count_others = 0
    for j in range(i, len(compressed)):
        if compressed[j][0] != num:
            count_others += compressed[j][1]
            if count_others > K:
                break
            continue
        count_num += compressed[j][1]
        if max_count < count_num:
            max_count = count_num

sys.stdout.write(str(max_count))