import sys

N, K = map(int, sys.stdin.readline().split())
compressed = []
pivot = {}
for num in map(int, sys.stdin.readline().split()):
    if num not in pivot:
        pivot[num] = []
    if compressed and compressed[-1][0] == num:
        compressed[-1][1] += 1
    else:
        pivot[num].append(len(compressed))
        compressed.append([num, 1])

max_series = 0
for num in pivot:
    for i in range(len(pivot[num])):
        l = pivot[num][i]
        for j in range(i, len(pivot[num])):
            r = pivot[num][j]
            removable = K
            series = 0
            # 모든 가능한 [l, r] 구간 내에서 num만 남기고 제거
            for k in range(l, r + 1):
                if compressed[k][0] != num:
                    removable -= compressed[k][1]
                    if removable < 0:
                        break
                    continue
                series += compressed[k][1]
            else:
                if max_series < series:
                    max_series = series 
                print(f'{num} - 보존 ({l}, {r}) 성공 - {series}')

sys.stdout.write(str(max_series))